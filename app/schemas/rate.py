from pydantic import BaseModel


class RateBase(BaseModel):
    name: str


class RateCreate(RateBase):
    pass


class RateOut(RateBase):
    id: str
