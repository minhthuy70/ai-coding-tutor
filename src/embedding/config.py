"""
Configuration Module for RAG Embedding Framework.
Defines model identifiers, resource parameters, and directory paths
compatible with both Kaggle Cloud GPU and local mock testing.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ModelConfig:
    """Configuration for a specific embedding model."""
    model_name: str
    model_id: str
    dimension: int
    context_length: int
    batch_size: int
    torch_dtype: str = "float16"  # "float16" | "bfloat16" | "float32"
    device: str = "cuda"           # "cuda" | "cpu"
    normalize_embeddings: bool = True
    query_instruction: Optional[str] = None
    extra_kwargs: dict = field(default_factory=dict)


@dataclass
class EmbeddingPipelineConfig:
    """Global configuration for the embedding pipeline."""
    # Input data paths (auto-fallback if on Kaggle or local)
    kaggle_input_dir: Path = Path("/kaggle/input/ai-coding-tutor-rag-data")
    local_data_path: Path = Path("data/06_rag_dataset/chunks/all_chunks.json")
    
    # Working & Output directories
    kaggle_working_dir: Path = Path("/kaggle/working")
    local_working_dir: Path = Path("data/08_rag_dataset")
    
    # Checkpoints
    checkpoint_dir_name: str = "checkpoints"
    embeddings_dir_name: str = "embeddings"
    reports_dir_name: str = "reports"
    checkpoint_every_batches: int = 5  # Save checkpoint every N batches
    
    # Modality Classification Rule: threshold 50.0% partitions exactly 937 CODE and 4,293 TEXT
    code_ratio_threshold: float = 0.50
    dataset_fingerprint: str = "sha256:4b969e117eac5c123756e4382cf3e0c7c7aeeba8ec8bb0d673e296532f35b856"
    
    # Model Configurations
    qwen3_text: ModelConfig = field(default_factory=lambda: ModelConfig(
        model_name="qwen3_text",
        model_id="Qwen/Qwen3-Embedding-0.6B",
        dimension=1024,
        context_length=32768,
        batch_size=32,
        torch_dtype="float16",
        query_instruction="Instruct: Given a programming question, coding task, or technical problem, retrieve relevant Python documentation, tutorials, code concepts, or API explanations.\nQuery: "
    ))
    
    jina_code: ModelConfig = field(default_factory=lambda: ModelConfig(
        model_name="jina_code",
        model_id="jinaai/jina-embeddings-v2-base-code",
        dimension=768,
        context_length=8192,
        batch_size=32,
        torch_dtype="float16",
        extra_kwargs={"trust_remote_code": True}
    ))
    
    jina_visual: ModelConfig = field(default_factory=lambda: ModelConfig(
        model_name="jina_visual",
        model_id="jinaai/jina-embeddings-v4",
        dimension=2048,  # Supports Matryoshka down to 768
        context_length=32768,
        batch_size=4,
        torch_dtype="bfloat16",
        extra_kwargs={"trust_remote_code": True}
    ))
    
    colqwen2_page: ModelConfig = field(default_factory=lambda: ModelConfig(
        model_name="colqwen2_page",
        model_id="vidore/colqwen2-v1.0-hf",
        dimension=128,  # Multi-vector patch dimension
        context_length=4096,
        batch_size=2,
        torch_dtype="bfloat16"
    ))

    def resolve_input_file(self) -> Path:
        """Resolve chunk input file with priority for Kaggle then local fallback."""
        kaggle_file = self.kaggle_input_dir / "all_chunks.json"
        if kaggle_file.exists():
            return kaggle_file
        
        # Check alternative Kaggle mount path
        alt_kaggle = Path("/kaggle/input/all_chunks.json")
        if alt_kaggle.exists():
            return alt_kaggle
            
        if self.local_data_path.exists():
            return self.local_data_path
            
        raise FileNotFoundError(
            f"Input chunk file not found at Kaggle ({kaggle_file}) or local ({self.local_data_path})"
        )

    def resolve_working_dir(self) -> Path:
        """Resolve working directory based on environment."""
        if Path("/kaggle/working").exists():
            return self.kaggle_working_dir
        return self.local_working_dir
