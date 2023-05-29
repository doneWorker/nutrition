import uvicorn
from fastapi import FastAPI

import config
from app.api.v1.endpoints import router

app = FastAPI()
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.get_settings().host, port=config.get_settings().port, reload=True)
