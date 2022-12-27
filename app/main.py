from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from . import models
# from .database import engine
from .routers import post, user, auth, vote


# we don't need it because of alembic does any migrations
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# we give possibility to send requests to our API from no-localhost domains. Example: 'https://www.google.com'
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# we use include_router to include path operations from different files after divided them
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello to web"}
