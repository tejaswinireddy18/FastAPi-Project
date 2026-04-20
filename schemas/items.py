from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str
    description: str = Field(default="")
    price: float = Field(gt=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
