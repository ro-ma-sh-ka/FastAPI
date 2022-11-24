from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello to"}


@app.get("/posts")
def get_posts():
    return {"data": "this is posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    return {"message": f"title {payload['title']} content {payload['content']}"}
