from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

##This class tells what a post should look like##this is pydantic check
class Post(BaseModel):
  title: str
  content: str
  published: bool= True
  rating: Optional[int] = None


my_posts = [{"title":"title of post 1", "content":"content of post 1", "id":1}, {"title":"favorite foods", "content":"I like your pizza", "id":2}]



@app.get("/")
def root():
  return {"message":"Hello"}

@app.get("/posts")
def get_post():
  return {"data":my_posts}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
  print(payload)
  return {"new_post":f"title: {payload['title']} content:{payload['content']}"}


@app.post("/mypost")
def my_post(post:Post):
 
  post_dict = post.model_dump()
  post_dict['id'] = randrange(0,1000000)
  my_posts.append(post_dict)
  return {"data":post_dict}  


##saving this post data...how??--simple , store it in a list as a dictionary





