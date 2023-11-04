from pydantic import BaseModel
from typing import Optional

# Esquema
class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    year: int
    director: str
    genre: str
    rating: float