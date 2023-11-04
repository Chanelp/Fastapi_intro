from pydantic import BaseModel, Field
from typing import Optional

# Esquema
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length= 5, max_length= 15)
    year: int = Field(le= 2023)
    director: str = Field(min_length= 3)
    genre: str
    rating: float
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "id": 1,
                "title": "Nombre de la peli",
                "director": "Quien la dirige",
                "year": 2023,
                "genre": "Género de peli",
                "rating": 9.0
            }
            ]
        }
   }