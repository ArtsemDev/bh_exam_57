from pydantic import BaseModel, Field


class ArticleCommentSchema(BaseModel):
    article_id: int = Field(ge=1)
    user_id: int = Field(ge=1)
    comment: str = Field(max_length=140)


class ArticleCommentInDBSchema(ArticleCommentSchema):
    id: int = Field(ge=1)
