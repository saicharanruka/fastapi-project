from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

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
    return {"data" : my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000)

    my_posts.append(post_dict)

    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {"message" : f"post with {id} was not found"}
    return {"post_details" : post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    value = None

    for i in range(0, len(my_posts)):
        if my_posts[i]['id'] == id:
            value = my_posts.pop(i)
            break
    
    if value is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found to delete")
    
    return {"post_details" : value}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts.append(post_dict)

    return {'message' : 'updated post'}