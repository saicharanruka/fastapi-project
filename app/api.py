import os
from pathlib import Path
from dotenv import load_dotenv

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

from random import randrange
import time

import psycopg
from psycopg.rows import dict_row


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

class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:
        conn = psycopg.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, row_factory=dict_row)

        cursor = conn.cursor()
        print("DB connection was successful!")
        break
    except Exception as error:
        print(error)
        time.sleep(2)



my_posts = [
    {"id" : 1, "title" : "title 1", "content" : "content for post 1"},
    {"id" : 2, "title" : "title 2", "content" : "content for post 2"},
    ]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


# Order of path operation matters as the first one with the path gets returned
@app.get("/")
async def root():
    return {"message": "Welcome to my API new"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data" : posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):

    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id=%s""", (str(id),))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {"message" : f"post with {id} was not found"}
    return {"post_details" : post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    # for i in range(0, len(my_posts)):
    #     if my_posts[i]['id'] == id:
    #         value = my_posts.pop(i)
    #         break
    
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found to delete")
    
    return {"post_details" : deleted_post}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content=%s, published=%s WHERE id = %s RETURNING *""",
     (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {'data' : updated_post}