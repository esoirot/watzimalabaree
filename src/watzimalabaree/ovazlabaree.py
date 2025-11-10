from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from watzimalabaree.tools.book_storage import (
    load_items, add_item, get_item, update_item, delete_item
)

router = APIRouter(prefix="/ovazlabaree", tags=["Ovazlabaree Library"])
BOOKS_FILE = "ovazlabaree"


class Book(BaseModel):
    id: int
    name: str = ""
    price: float = 0.0
    has_barcode: bool = True


@router.get("/books/")
def list_books():
    return load_items(Book, BOOKS_FILE)


@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = get_item(Book, book_id, BOOKS_FILE)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/books/")
def create_book(book: Book):
    add_item(book, BOOKS_FILE)
    return book


@router.put("/books/{book_id}")
def modify_book(book_id: int, book: Book):
    updated = update_item(Book, book_id, book, BOOKS_FILE)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{book_id}")
def remove_book(book_id: int):
    deleted = delete_item(Book, book_id, BOOKS_FILE)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True}
