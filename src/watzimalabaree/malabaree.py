from typing import Dict, List

from fastapi import APIRouter, HTTPException

from watzimalabaree.models.item import Item
from watzimalabaree.tools.item_storage import (
    add_item,
    delete_item,
    get_item,
    load_items,
    update_item,
)

router = APIRouter(prefix="/malabaree", tags=["Malabaree Library"])
ITEMS_FILE = "malabaree"


# ----- Routes -----
@router.get("/items/", response_model=List[Item])
def list_malabaree_items() -> List[Item]:
    return load_items(Item, ITEMS_FILE)


@router.get("/items/{item_id}", response_model=Item)
def get_malabaree_item(item_id: int) -> Item:
    item = get_item(Item, item_id, ITEMS_FILE)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items/", response_model=Item)
def create_malabaree_item(item: Item) -> Item:
    add_item(item, ITEMS_FILE)
    return item


@router.put("/items/{item_id}", response_model=Item)
def modify_malabaree_item(item_id: int, item: Item) -> Item:
    updated = update_item(Item, item_id, item, ITEMS_FILE)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}", response_model=Dict[str, bool])
def remove_malabaree_item(item_id: int) -> Dict[str, bool]:
    deleted = delete_item(Item, item_id, ITEMS_FILE)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"ok": True}
