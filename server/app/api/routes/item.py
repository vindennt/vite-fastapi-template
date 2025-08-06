from uuid import UUID

from fastapi import APIRouter

from app.api.dependencies import CurrentUser, CurrentSession
from app.db.crud.item_crud import item
from app.db.models.item import Item, ItemCreate, ItemUpdate

router = APIRouter(prefix="/item", tags=["items"])

# CRUD operations for Item model

@router.post("/create-item")
async def create_item(
    item_in: ItemCreate, user: CurrentUser, session: CurrentSession
) -> Item:
    return item.create(session, owner_id=UUID(user.id), obj_in=item_in)


@router.get("/get-item/{id}")
async def read_item_by_id(id: str, session: CurrentSession) -> Item | None:
    return item.get(session, id=UUID(id))


@router.get("/get-items")
async def read_items(
    session: CurrentSession, skip: int = 0, limit: int = 100
) -> list[Item]:
    return list(item.get_multi(session, skip=skip, limit=limit))


@router.put("/update-item/{id}")
async def update_item(id: str, item_in: ItemUpdate, session: CurrentSession) -> Item | None:
    return item.update(session, id=UUID(id), obj_in=item_in)


@router.delete("/delete/{id}")
async def delete_item(id: str, session: CurrentSession) -> Item | None:
    return item.remove(session, id=UUID(id))
