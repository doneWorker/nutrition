import uvicorn
from fastapi import FastAPI

import config
from app.api import products

app = FastAPI()
app.include_router(products)

if __name__ == "__main__":
    uvicorn.run(app, host=config.Settings.db_url)
