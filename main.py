from fastapi import FastAPI

from api.v1 import api_v1_router


openapi_tags = [
    {
        'name': 'Article'
    }
]


app = FastAPI(
    title="BelHard EXAM",
    description='Group 57 exam project',
    version='bh57',
    openapi_tags=openapi_tags
)
app.include_router(api_v1_router)
