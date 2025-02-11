from fastapi import APIRouter, HTTPException
from database import books

router = APIRouter()

# Get all books
@router.get("/api/v1/books/")
async def get_all_books():
    return books

# Get a single book by ID
@router.get("/api/v1/books/{book_id}")
async def get_book_by_id(book_id: int):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Create a new book
@router.post("/api/v1/books/", status_code=201)
async def create_book(book: dict):
    books.append(book)
    return book

# Update a book
@router.put("/api/v1/books/{book_id}")
async def update_book(book_id: int, updated_book: dict):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@router.delete("/api/v1/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
