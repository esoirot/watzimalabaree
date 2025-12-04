from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str = ""
    price: float = 0.0
    has_barcode: bool = True
