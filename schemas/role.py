from pydantic import BaseModel, Field


class RoleInDBSchema(BaseModel):
    id: int = Field(ge=1)
    name: str = Field(max_length=45)
