from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import Article, create_async_session
from schemas import ArticleSchema, ArticleInDBSchema


class CRUDArticle:

    @staticmethod
    @create_async_session
    async def add(article: ArticleSchema, session: AsyncSession = None) -> ArticleInDBSchema | None:
        article = Article(**article.dict())
        session.add(article)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article)
            return ArticleInDBSchema(**article.__dict__)

    @staticmethod
    @create_async_session
    async def get(article_id: int, session: AsyncSession = None) -> ArticleInDBSchema | None:
        article = await session.execute(
            select(Article)
            .where(Article.id == article_id)
        )
        if article := article.first():
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(category_id: int = None, session: AsyncSession = None) -> list[ArticleInDBSchema]:
        if category_id:
            articles = await session.execute(
                select(Article)
                .where(Article.category_id == category_id)
            )
        else:
            articles = await session.execute(
                select(Article)
            )
        return [ArticleInDBSchema(**article[0].__dict__) for article in articles]
