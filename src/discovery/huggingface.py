import json
from pathlib import Path
from typing import Any

import requests

from src.schemas import AIModel


HUGGING_FACE_API = "https://huggingface.co/api/models"


def search_models(
    search: str = "text-generation",
    limit: int = 10
) -> list[dict[str, Any]]:

    params = {
        "search": search,
        "limit": limit,
        "sort": "downloads",
        "direction": -1,
    }

    response = requests.get(
        HUGGING_FACE_API,
        params=params,
        timeout=20,
    )

    response.raise_for_status()

    return response.json()


def model_to_entity(
    model: dict[str, Any]
) -> AIModel:

    model_id = model.get("id", "unknown")

    return AIModel(
        name=model_id,
        description="",
        url=f"https://huggingface.co/{model_id}",
        categories=["ai", "model"],
        source={
            "name": "Hugging Face",
            "url": "https://huggingface.co",
        },
    )


def save_raw_models(
    models: list[dict[str, Any]]
) -> str:

    output_dir = Path("data/raw")
    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / "huggingface.json"

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            models,
            file,
            indent=2,
            ensure_ascii=False
        )

    return str(output_file)