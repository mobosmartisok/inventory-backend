"""منطق کسب‌وکار Rate -- جدا از لایهٔ مسیر و لایهٔ داده."""
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.errors import AppError
from app.repositories.rate import RateRepository
from app.schemas.rate import RateCreate, RateOut


async def list_rates(db: AsyncSession) -> List[RateOut]:
    return await RateRepository(db).list()


async def get_rate(db: AsyncSession, item_id: str) -> RateOut:
    item = await RateRepository(db).get(item_id)
    if item is None:
        raise AppError("not_found", "Rate پیدا نشد", status_code=404)
    return item


async def create_rate(db: AsyncSession, payload: RateCreate) -> RateOut:
    return await RateRepository(db).create(payload.model_dump())


async def delete_rate(db: AsyncSession, item_id: str) -> None:
    await get_rate(db, item_id)
    await RateRepository(db).delete(item_id)
