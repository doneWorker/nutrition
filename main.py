import uvicorn
from fastapi import FastAPI

import config
from app.api.products import productsRouter
from app.modules.users.router import usersRouter

app = FastAPI()
app.include_router(productsRouter)
app.include_router(usersRouter)

if __name__ == "__main__":
    uvicorn.run(app, host=config.get_settings().host, port=config.get_settings().port)
