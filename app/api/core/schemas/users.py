from typing import Generic

from fastapi_users import models
from fastapi_users.schemas import CreateUpdateDictModel, PYDANTIC_V2
from pydantic import ConfigDict, EmailStr


class UserRead(CreateUpdateDictModel, Generic[models.ID]):
    id: models.ID
    email: EmailStr

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class UserCreate(CreateUpdateDictModel):
    email: EmailStr
    password: str
