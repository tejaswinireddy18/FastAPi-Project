from fastapi import APIRouter, HTTPException, status

from schemas.items import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter()

items_db: dict[int, ItemResponse] = {}
next_item_id = 1


@router.get("/", response_model=list[ItemResponse])
def get_items() -> list[ItemResponse]:
    return list(items_db.values())


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> ItemResponse:
    global next_item_id
    new_item = ItemResponse(id=next_item_id, **payload.model_dump())
    items_db[next_item_id] = new_item
    next_item_id += 1
    return new_item


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, payload: ItemUpdate) -> ItemResponse:
    existing_item = items_db.get(item_id)
    if existing_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    updated_data = existing_item.model_dump()
    updated_data.update(payload.model_dump())
    updated_item = ItemResponse(**updated_data)
    items_db[item_id] = updated_item
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    del items_db[item_id]
