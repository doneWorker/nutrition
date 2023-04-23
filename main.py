import uvicorn
from fastapi import FastAPI

import config
from app.api.products import productsRouter

app = FastAPI()
app.include_router(productsRouter)

if __name__ == "__main__":
    uvicorn.run(app, host=config.get_settings().host, port=config.get_settings().port)
