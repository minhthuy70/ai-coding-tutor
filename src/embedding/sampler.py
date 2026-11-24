"""
Deterministic Pilot Sampler Module.
Selects representative sample chunks for Kaggle GPU Pilot testing:
- Pilot A: 120 TEXT chunks (stratified across 23 source files, seed=42)
- Pilot B: 40 CODE chunks (30 code_example + 10 mixed code chunks >= 50%, seed=42)
Total: 160 pilot chunks.
"""

import json
import logging
import random
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from .base import Modality
from .router import ModalityRouter

logger = logging.getLogger("PilotSampler")


class PilotSampler:
    """
    Deterministic sampler for Phase 3 Kaggle GPU Pilot.
    Guarantees 100% reproducibility via fixed random seed.
    """

    def __init__(self, seed: int = 42, router: Optional[ModalityRouter] = None):
        self.seed = seed
        self.router = router or ModalityRouter(code_ratio_threshold=0.50)

    def sample_pilot_dataset(
        self,
        chunks: List[dict],
        text_limit: int = 120,
        code_limit: int = 40,
        code_mixed_count: int = 10
    ) -> Dict[str, any]:
        """
        Sample exactly text_limit TEXT chunks and code_limit CODE chunks.
        """
        rng = random.Random(self.seed)
        routed = self.router.route_chunks(chunks)
        text_chunks = routed[Modality.TEXT]
        code_chunks = routed[Modality.CODE]

        # 1. Stratified sampling for TEXT chunks across source_file
        text_by_file = defaultdict(list)
        for c in text_chunks:
            sfile = c.get("metadata", {}).get("source_file", "unknown")
            text_by_file[sfile].append(c)

        sampled_text = []
        total_text = len(text_chunks)
        remaining = text_limit

        for sfile, flist in sorted(text_by_file.items()):
            # Proportionate count with at least 1 per file where possible
            count = max(1, round(len(flist) / total_text * text_limit))
            count = min(count, len(flist), remaining)
            flist_copy = list(flist)
            rng.shuffle(flist_copy)
            sampled_text.extend(flist_copy[:count])
            remaining -= count

        # Adjust any rounding discrepancy
        if len(sampled_text) < text_limit:
            used_ids = {x["id"] for x in sampled_text}
            unused = [c for c in text_chunks if c["id"] not in used_ids]
            rng.shuffle(unused)
            sampled_text.extend(unused[:text_limit - len(sampled_text)])
        elif len(sampled_text) > text_limit:
            sampled_text = sampled_text[:text_limit]

        # 2. Balanced sampling for CODE chunks (code_example + mixed >= 50%)
        code_example = [
            c for c in code_chunks
            if c.get("metadata", {}).get("content_type") == "code_example"
        ]
        code_mixed = [
            c for c in code_chunks
            if c.get("metadata", {}).get("content_type") != "code_example"
        ]

        target_mixed = min(code_mixed_count, len(code_mixed))
        target_example = code_limit - target_mixed

        rng.shuffle(code_example)
        rng.shuffle(code_mixed)

        sampled_code = code_example[:target_example] + code_mixed[:target_mixed]

        logger.info(
            f"Pilot Sampling completed (seed={self.seed}): "
            f"TEXT = {len(sampled_text)} (from {len(text_by_file)} files), "
            f"CODE = {len(sampled_code)} ({target_example} code_example + {target_mixed} mixed)."
        )

        return {
            "seed": self.seed,
            "text_chunks": sampled_text,
            "code_chunks": sampled_code,
            "total_chunks": len(sampled_text) + len(sampled_code)
        }

    def export_pilot_file(
        self,
        chunks: List[dict],
        output_path: Path,
        text_limit: int = 120,
        code_limit: int = 40
    ) -> Path:
        """Export the unified 160 pilot chunks to a standalone JSON file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        pilot_data = self.sample_pilot_dataset(
            chunks, text_limit=text_limit, code_limit=code_limit
        )
        combined_chunks = pilot_data["text_chunks"] + pilot_data["code_chunks"]

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(combined_chunks, f, ensure_ascii=False, indent=2)

        logger.info(f"Exported {len(combined_chunks)} pilot chunks to {output_path}")
        return output_path
