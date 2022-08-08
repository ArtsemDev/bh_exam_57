from pydantic import BaseModel, Field


class ConfigSchema(BaseModel):
    DATABASE: str
