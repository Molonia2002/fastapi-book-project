from fastapi import APIRouter, HTTPException
from database import books

router = APIRouter()

@router.get("/api/v1/books/{book_id}")
async def get_book_by_id(book_id: int): 
	book = next((book for book in books if book["id"] == book_id), None)
	
	if not book: 
		raise HTTPException(status_code=404, detail="Book not found") 
	
	return book 
