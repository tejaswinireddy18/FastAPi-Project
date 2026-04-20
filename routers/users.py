from fastapi import APIRouter, HTTPException, status

from schemas.users import UserCreate, UserResponse, UserUpdate

router = APIRouter()

users_db: dict[int, UserResponse] = {}
next_user_id = 1


@router.get("/", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    return list(users_db.values())


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> UserResponse:
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> UserResponse:
    global next_user_id
    new_user = UserResponse(id=next_user_id, **payload.model_dump())
    users_db[next_user_id] = new_user
    next_user_id += 1
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, payload: UserUpdate) -> UserResponse:
    existing_user = users_db.get(user_id)
    if existing_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    updated_data = existing_user.model_dump()
    updated_data.update(payload.model_dump())
    updated_user = UserResponse(**updated_data)
    users_db[user_id] = updated_user
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    del users_db[user_id]
