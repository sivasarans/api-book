from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    published_date: str

books = []

@app.post("/api_books/", response_model=Book)
def create_book(book:List[ Book]):
    books.extend(book)
    return book

@app.get("/api_books/", response_model=List[Book])
def get_books():
    return books
