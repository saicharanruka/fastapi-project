import os
from pathlib import Path
from dotenv import load_dotenv

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional

from random import randrange
import time

import psycopg
from psycopg.rows import dict_row

from sqlalchemy.orm import Session
from . import models, utils
from .database import engine, get_db
from .schemas import Post, UserCreate, UserResponse
from .routers import post, user, auth



models.Base.metadata.create_all(bind=engine)


# Loading environment variables ----
ROOT_DIR = Path(__file__).parent.parent
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)


DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
# ---------------

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)




# V2 -----------------
# while True:
#     try:
#         conn = psycopg.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, row_factory=dict_row)

#         cursor = conn.cursor()
#         print("DB connection was successful!")
#         break
#     except Exception as error:
#         print(error)
#         time.sleep(2)


# V1 ------------------
# my_posts = [
#     {"id" : 1, "title" : "title 1", "content" : "content for post 1"},
#     {"id" : 2, "title" : "title 2", "content" : "content for post 2"},
#     ]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# Order of path operation matters as the first one with the path gets returned
@app.get("/")
async def root():
    return {"message": "Welcome to my API new"}



# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
    
#     posts = db.query(models.Post).all()
#     return {"data" : posts}
