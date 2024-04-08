from time import time

from fastapi import FastAPI, Request

from app.api_v1.routers import api_v1_router
from app.core.config import settings
from app.logger import logger


app = FastAPI(title=settings.app_title, description=settings.app_description)
app.include_router(api_v1_router)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    """Middleware для логирования запросов."""
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time

    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "status": response.status_code,
        "process_time": process_time,
    }
    logger.info(log_dict)

    return response
