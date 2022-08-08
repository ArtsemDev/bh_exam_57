from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    login: str = Field(min_length=8, max_length=24)
    hashed_password: str
    email: str = Field(max_length=45)
    role_id: int = Field(ge=1)


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
