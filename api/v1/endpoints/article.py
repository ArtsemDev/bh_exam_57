from fastapi import APIRouter, HTTPException, Query

from schemas import ArticleSchema, ArticleInDBSchema
from crud import CRUDArticle


article_router = APIRouter(prefix='/article', tags=['Article'])


@article_router.put('/add', response_model=ArticleInDBSchema, status_code=201)
async def add_article(article: ArticleSchema):
    if article := await CRUDArticle.add(article=article):
        return article
    raise HTTPException(status_code=400)


@article_router.get('/get', response_model=ArticleInDBSchema)
async def get_article(article_id: int = Query(ge=1)):
    article = await CRUDArticle.get(article_id=article_id)
    if article:
        return article
    raise HTTPException(status_code=404)


@article_router.get(
    '/all',
    description='Getting all articles, if the `category_id` attribute is passed, then articles for this category, if not passed, then absolutely all articles'
)
async def get_all(category_id: int = Query(ge=1, default=None)):
    articles = await CRUDArticle.get_all(category_id=category_id)
    return articles

