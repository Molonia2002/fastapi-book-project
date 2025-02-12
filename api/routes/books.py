from collections import OrderedDict
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre, InMemoryDB

router = APIRouter()

# Initialize in-memory database
db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.FANTASY,  # Fixed Genre
    ),
    2: Book(
        id=2,
        title="1984",
        author="George Orwell",
        publication_year=1949,
        genre=Genre.SCI_FI,  # Fixed Genre
    ),
    3: Book(
        id=3,
        title="To Kill a Mockingbird",
        author="Harper Lee",
        publication_year=1960,
        genre=Genre.MYSTERY,  # Fixed Genre
    ),
}


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """
    Retrieve a book by its ID.
    """
    book = db.books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    """
    Add a new book to the database.
    """
    db.add_book(book)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=book.model_dump())


@router.get("/", response_model=list[Book], status_code=status.HTTP_200_OK)
async def get_books():
    """
    Retrieve all books as a list.
    """
    return list(db.books.values())  # Fix: Return list instead of dict


@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book):
    """
    Update a book's details.
    """
    return db.update_book(book_id, book)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    """
    Delete a book by ID.
    """
    db.delete_book(book_id)
    return None
