from app import  app
from app.api import master

app.include_router(
    master.router,
    prefix='/api'
)

