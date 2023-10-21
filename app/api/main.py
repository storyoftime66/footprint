from fastapi import FastAPI
from models.photo import Photo

api = FastAPI()


@api.get("/")
def read_root():
    return "root"

@api.get("/photos/")
def read_photos():
    return Photo()