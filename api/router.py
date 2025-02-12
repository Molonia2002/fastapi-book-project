from fastapi import APIRouter, HTTPException
from typing import List
from api.db import books

router = APIRouter()

@router.get("/api/v1/books/", response_model=List[dict])
def get_all_books():
    return books

@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# ✅ ADD MISSING ENDPOINTS
@router.post("/books/", status_code=201)
def create_book(book: dict):
    books.append(book)
    return book

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return
