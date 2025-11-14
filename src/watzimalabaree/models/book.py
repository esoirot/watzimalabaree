# ----- Model -----
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str = ""
    price: float = 0.0
    has_barcode: bool = True
