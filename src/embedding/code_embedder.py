"""
Jina Code Embedder Wrapper.
Implements code-specialized dense embedding for Python, AST structures, and programming logic.
"""

import logging
from typing import List, Optional
from .base import BaseEmbedder
from .config import ModelConfig

logger = logging.getLogger("JinaCodeEmbedder")


class JinaCodeEmbedder(BaseEmbedder):
    """
    Wrapper for jinaai/jina-embeddings-v2-base-code.
    Dynamic import of sentence-transformers inside load_model() for local safety.
    """

    def __init__(self, config: ModelConfig):
        super().__init__(config)
        self.model = None

    def load_model(self) -> None:
        """Load Jina Code Embeddings v2 checkpoint on Kaggle GPU."""
        if self._is_loaded:
            return

        logger.info(f"Loading Jina Code checkpoint: {self.config.model_id}...")
        try:
            # Compatibility patch for JinaBert in recent transformers versions
            import transformers.pytorch_utils
            if not hasattr(transformers.pytorch_utils, "find_pruneable_heads_and_indices"):
                def find_pruneable_heads_and_indices(heads, n_heads, head_size, already_pruned_heads):
                    import torch
                    mask = torch.ones(n_heads, head_size)
                    heads = set(heads) - already_pruned_heads
                    for head in heads:
                        head = head - sum(1 if h < head else 0 for h in already_pruned_heads)
                        mask[head] = 0
                    mask = mask.view(-1).contiguous().eq(1)
                    index: torch.LongTensor = torch.arange(len(mask))[mask].long()
                    return heads, index
                transformers.pytorch_utils.find_pruneable_heads_and_indices = find_pruneable_heads_and_indices

            from transformers import PretrainedConfig
            for _attr, _default in [("is_decoder", False), ("add_cross_attention", False), ("chunk_size_feed_forward", 0), ("pruned_heads", set()), ("use_return_dict", True)]:
                if not hasattr(PretrainedConfig, _attr):
                    setattr(PretrainedConfig, _attr, _default)

            from transformers.modeling_utils import PreTrainedModel
            import torch
            if not hasattr(PreTrainedModel, "get_head_mask"):
                def get_head_mask(self, head_mask, num_hidden_layers, is_attention_chunked=False):
                    if head_mask is not None:
                        if head_mask.dim() == 1: head_mask = head_mask.unsqueeze(0).unsqueeze(0).unsqueeze(-1).unsqueeze(-1).expand(num_hidden_layers, -1, -1, -1, -1)
                        elif head_mask.dim() == 2: head_mask = head_mask.unsqueeze(1).unsqueeze(-1).unsqueeze(-1)
                        return head_mask.to(dtype=getattr(self, "dtype", torch.float32))
                    return [None] * num_hidden_layers
                PreTrainedModel.get_head_mask = get_head_mask

            if not hasattr(PreTrainedModel, "get_extended_attention_mask"):
                def get_extended_attention_mask(self, attention_mask, input_shape, dtype=None):
                    if dtype is None: dtype = getattr(self, "dtype", torch.float32)
                    if attention_mask.dim() == 3: extended_mask = attention_mask[:, None, :, :]
                    elif attention_mask.dim() == 2: extended_mask = attention_mask[:, None, None, :]
                    else: raise ValueError(f"Wrong attention_mask shape: {attention_mask.shape}")
                    extended_mask = extended_mask.to(dtype=dtype)
                    return (1.0 - extended_mask) * -10000.0
                PreTrainedModel.get_extended_attention_mask = get_extended_attention_mask

            if not hasattr(PreTrainedModel, "invert_attention_mask"):
                def invert_attention_mask(self, encoder_attention_mask):
                    if encoder_attention_mask.dim() == 3: ext = encoder_attention_mask[:, None, :, :]
                    elif encoder_attention_mask.dim() == 2: ext = encoder_attention_mask[:, None, None, :]
                    else: ext = encoder_attention_mask
                    ext = ext.to(dtype=getattr(self, "dtype", torch.float32))
                    return (1.0 - ext) * -10000.0
                PreTrainedModel.invert_attention_mask = invert_attention_mask

            from sentence_transformers import SentenceTransformer
        except ImportError as e:
            raise RuntimeError(
                f"sentence-transformers not installed ({e}). "
                "Ensure execution occurs within Kaggle environment."
            )

        model_kwargs = self.config.extra_kwargs.get("model_kwargs", {})
        model_kwargs.setdefault("attn_implementation", "eager")

        self.model = SentenceTransformer(
            self.config.model_id,
            trust_remote_code=self.config.extra_kwargs.get("trust_remote_code", True),
            model_kwargs=model_kwargs,
            device=self.config.device
        )
        self._is_loaded = True
        logger.info(f"Jina Code model successfully loaded. Dimension: {self.config.dimension}")

    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        """Encode code snippets into 768-dim normalized vectors with OOM protection."""
        if not self._is_loaded:
            self.load_model()

        bs = batch_size or self.config.batch_size
        try:
            embeddings = self.model.encode(
                texts,
                batch_size=bs,
                show_progress_bar=False,
                normalize_embeddings=self.config.normalize_embeddings,
                convert_to_numpy=True
            )
            return embeddings.tolist()
        except Exception as e:
            # Check for CUDA OOM
            if "out of memory" in str(e).lower() or "CUDA out of memory" in str(e):
                logger.warning(f"CUDA OOM in JinaCodeEmbedder with batch_size {bs}. Retrying with batch_size=8...")
                try:
                    import torch
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                except ImportError:
                    pass
                embeddings = self.model.encode(
                    texts,
                    batch_size=max(1, bs // 4),
                    show_progress_bar=False,
                    normalize_embeddings=self.config.normalize_embeddings,
                    convert_to_numpy=True
                )
                return embeddings.tolist()
            raise e

    def embed_query(self, query: str) -> List[float]:
        """Encode query for code retrieval."""
        return self.embed_documents([query])[0]

    def unload_model(self) -> None:
        """Release VRAM."""
        if self._is_loaded:
            del self.model
            self.model = None
            self._is_loaded = False
            try:
                import torch
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except ImportError:
                pass
            logger.info("Unloaded Jina Code model and freed GPU cache.")
