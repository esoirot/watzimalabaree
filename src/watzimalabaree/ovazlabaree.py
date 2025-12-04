from typing import Dict, List

from fastapi import APIRouter, HTTPException

from watzimalabaree.models.book import Book
from watzimalabaree.tools.item_storage import (
    add_item,
    delete_item,
    get_item,
    load_items,
    update_item,
)

router = APIRouter(prefix="/ovazlabaree", tags=["Ovazlabaree Library"])
BOOKS_FILE = "ovazlabaree"


# ----- Routes -----
@router.get("/books/", response_model=List[Book])
def list_books() -> List[Book]:
    return load_items(Book, BOOKS_FILE)


@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    book = get_item(Book, book_id, BOOKS_FILE)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/books/", response_model=Book)
def create_book(book: Book) -> Book:
    add_item(book, BOOKS_FILE)
    return book


@router.put("/books/{book_id}", response_model=Book)
def modify_book(book_id: int, book: Book) -> Book:
    updated = update_item(Book, book_id, book, BOOKS_FILE)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{book_id}", response_model=Dict[str, bool])
def remove_book(book_id: int) -> Dict[str, bool]:
    deleted = delete_item(Book, book_id, BOOKS_FILE)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True}
