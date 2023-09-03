from fastapi import FastAPI, Depends

from orders.config import get_settings, Settings


app = FastAPI()

from orders.api import api


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
