from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, SmallInteger, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(45), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))


class Role(Base):
    __tablename__: str = 'roles'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(45), unique=True, nullable=False)


class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(VARCHAR(24), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    email = Column(VARCHAR(45), unique=True, nullable=False)
    role_id = Column(SmallInteger, ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)


class Article(Base):
    __tablename__: str = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(45), nullable=False)
    body = Column(VARCHAR(1024), nullable=False)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


class ArticleComment(Base):
    __tablename__: str = 'article_comments'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    comment = Column(VARCHAR(140), nullable=False)
