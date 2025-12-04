from watzimalabaree.models.item import Item


class BoardGame(Item):
    id: int
    name: str = ""
    price: float = 0.0
    has_barcode: bool = True
