"""لایهٔ داده برای Rate -- Postgres (SQLAlchemy async)."""
import uuid
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.rate import RateModel
from app.schemas.rate import RateOut


def _to_schema(row: RateModel) -> RateOut:
    return RateOut(
        id=row.id,
        name=row.name,
    )


class RateRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def list(self) -> List[RateOut]:
        result = await self.db.execute(select(RateModel))
        return [_to_schema(row) for row in result.scalars().all()]

    async def get(self, item_id: str) -> Optional[RateOut]:
        row = await self.db.get(RateModel, item_id)
        return _to_schema(row) if row else None

    async def create(self, data: dict) -> RateOut:
        row = RateModel(id=str(uuid.uuid4()), **data)
        self.db.add(row)
        await self.db.commit()
        await self.db.refresh(row)
        return _to_schema(row)

    async def delete(self, item_id: str) -> None:
        row = await self.db.get(RateModel, item_id)
        if row:
            await self.db.delete(row)
            await self.db.commit()
