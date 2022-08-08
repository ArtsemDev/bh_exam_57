from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    title: str = Field(max_length=45)
    body: str = Field(max_legth=1024)
    category_id: int = Field(ge=1)
    user_id: int = Field(ge=1)


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)
