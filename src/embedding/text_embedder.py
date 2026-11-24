"""
Qwen3 Text Embedder Wrapper.
Implements the official Qwen3-Embedding-0.6B architecture with last_token_pool
and task instructions for multilingual and programming theory retrieval.
"""

import logging
from typing import List, Optional
from .base import BaseEmbedder
from .config import ModelConfig

logger = logging.getLogger("Qwen3TextEmbedder")


class Qwen3TextEmbedder(BaseEmbedder):
    """
    Wrapper for Qwen/Qwen3-Embedding-0.6B.
    Note: Heavy libraries (torch, transformers) are dynamically imported inside load_model()
    to guarantee local machine safety.
    """

    def __init__(self, config: ModelConfig):
        super().__init__(config)
        self.tokenizer = None
        self.model = None

    def _last_token_pool(self, last_hidden_states, attention_mask):
        """Official pooling method recommended by Qwen team for Qwen3-Embedding."""
        import torch
        left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
        if left_padding:
            return last_hidden_states[:, -1]
        else:
            sequence_lengths = attention_mask.sum(dim=1) - 1
            batch_size = last_hidden_states.shape[0]
            return last_hidden_states[
                torch.arange(batch_size, device=last_hidden_states.device),
                sequence_lengths
            ]

    def load_model(self) -> None:
        """Load Qwen3-Embedding-0.6B on Kaggle Cloud GPU."""
        if self._is_loaded:
            return

        logger.info(f"Loading Qwen3 model checkpoint: {self.config.model_id} on {self.config.device}...")
        try:
            import torch
            from transformers import AutoModel, AutoTokenizer
        except ImportError as e:
            raise RuntimeError(
                f"Required deep learning libraries not found ({e}). "
                "Ensure this code runs within Kaggle Cloud environment."
            )

        dtype_map = {
            "float16": torch.float16,
            "bfloat16": torch.bfloat16,
            "float32": torch.float32
        }
        torch_dtype = dtype_map.get(self.config.torch_dtype, torch.float16)

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.config.model_id,
            padding_side="left"
        )
        self.model = AutoModel.from_pretrained(
            self.config.model_id,
            torch_dtype=torch_dtype,
            device_map="auto" if self.config.device == "cuda" else None
        )
        if self.config.device == "cuda" and not hasattr(self.model, "hf_device_map"):
            self.model = self.model.to("cuda")

        self.model.eval()
        self._is_loaded = True
        logger.info(f"Qwen3 model successfully loaded. Dimensionality: {self.config.dimension}")

    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        """Encode a batch of document texts into dense 1024-dim vectors."""
        if not self._is_loaded:
            self.load_model()

        import torch
        import torch.nn.functional as F

        bs = batch_size or self.config.batch_size
        all_embeddings: List[List[float]] = []

        with torch.no_grad():
            for i in range(0, len(texts), bs):
                batch_texts = texts[i:i + bs]
                try:
                    inputs = self.tokenizer(
                        batch_texts,
                        max_length=self.config.context_length,
                        padding=True,
                        truncation=True,
                        return_tensors="pt"
                    ).to(self.model.device)

                    outputs = self.model(**inputs)
                    embeddings = self._last_token_pool(outputs.last_hidden_state, inputs["attention_mask"])

                    if self.config.normalize_embeddings:
                        embeddings = F.normalize(embeddings, p=2, dim=1)

                    all_embeddings.extend(embeddings.cpu().to(torch.float32).tolist())
                except torch.cuda.OutOfMemoryError:
                    logger.warning(f"CUDA OOM with batch size {len(batch_texts)}. Clearing cache and retrying individually...")
                    torch.cuda.empty_cache()
                    for single_text in batch_texts:
                        s_in = self.tokenizer(
                            [single_text],
                            max_length=self.config.context_length,
                            padding=True,
                            truncation=True,
                            return_tensors="pt"
                        ).to(self.model.device)
                        s_out = self.model(**s_in)
                        s_emb = self._last_token_pool(s_out.last_hidden_state, s_in["attention_mask"])
                        if self.config.normalize_embeddings:
                            s_emb = F.normalize(s_emb, p=2, dim=1)
                        all_embeddings.extend(s_emb.cpu().to(torch.float32).tolist())

        return all_embeddings

    def embed_query(self, query: str) -> List[float]:
        """Encode query using the required task instruction prefix."""
        instruction = self.config.query_instruction or ""
        formatted_query = f"{instruction}{query}"
        return self.embed_documents([formatted_query])[0]

    def unload_model(self) -> None:
        """Release VRAM and delete model reference."""
        if self._is_loaded:
            del self.model
            del self.tokenizer
            self.model = None
            self.tokenizer = None
            self._is_loaded = False
            try:
                import torch
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except ImportError:
                pass
            logger.info("Unloaded Qwen3 model and freed GPU cache.")
