import json
from pathlib import Path
from typing import Any, List, Optional, Type, TypeVar

from pydantic import BaseModel

# Generic type for any Pydantic model
T = TypeVar("T", bound=BaseModel)

# Base directory where all JSON files will live
JSONS_DIR: Path = Path(__file__).parent / "jsons"
JSONS_DIR.mkdir(parents=True, exist_ok=True)


# ---------- Generic storage functions ----------


def get_json_path(filename: str) -> Path:
    """Return the full path to a JSON file inside the jsons directory."""
    if not filename.endswith(".json"):
        filename += ".json"
    return JSONS_DIR / filename


def load_items(model: Type[T], filename: str) -> List[T]:
    """Load items from a JSON file as model instances."""
    file_path: Path = get_json_path(filename)
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        data: list[dict[str, Any]] = json.load(f)
    return [model(**b) for b in data]


def save_items(items: List[T], filename: str) -> None:
    """Save items (list of models) into a JSON file."""
    file_path: Path = get_json_path(filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([item.model_dump() for item in items], f, indent=4)


def get_item(model: Type[T], item_id: int, filename: str) -> Optional[T]:
    """Find one item by ID."""
    items: List[T] = load_items(model, filename)
    for item in items:
        if getattr(item, "id", None) == item_id:
            return item
    return None


def add_item(item: T, filename: str) -> None:
    """Add an item to the given JSON file."""
    items: List[T] = load_items(type(item), filename)
    items.append(item)
    save_items(items, filename)


def update_item(model: Type[T], item_id: int, updated_item: T, filename: str) -> bool:
    """Update an item by ID."""
    items: List[T] = load_items(model, filename)
    for i, item in enumerate(items):
        if getattr(item, "id", None) == item_id:
            items[i] = updated_item
            save_items(items, filename)
            return True
    return False


def delete_item(model: Type[T], item_id: int, filename: str) -> bool:
    """Delete an item by ID."""
    items: List[T] = load_items(model, filename)
    new_items: List[T] = [item for item in items if getattr(item, "id", None) != item_id]
    if len(new_items) == len(items):
        return False
    save_items(new_items, filename)
    return True
