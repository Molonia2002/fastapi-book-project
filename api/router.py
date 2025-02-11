from fastapi import APIRouter, HTTPException
from typing import List
from db import books  # Assuming books data is stored in db.py

router = APIRouter()

@router.get("/books/", response_model=List[dict])
def get_all_books():
    return books

@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
