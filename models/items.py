from dataclasses import dataclass


@dataclass
class ItemModel:
    id: int
    name: str
    description: str
    price: float
