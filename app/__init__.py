from fastapi import FastAPI
from .core.database import  DB

app = FastAPI()

DB.init()

from . import routes