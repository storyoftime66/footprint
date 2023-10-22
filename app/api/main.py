from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models
from db.database import SessionLocal, engine
import schemas

models.Base.metadata.create_all(bind=engine)

api = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.get("/")
def read_root():
    return "root"


@api.get("/photos/", response_model=list[schemas.photo.Photo])
def read_photos(db: Session = Depends(get_db)):
    return crud.get_photos(db)


@api.get("/photos/", response_model=list[schemas.photo.Photo])
def read_photo_by_id(photographer: str, db: Session = Depends(get_db)):
    return crud.get_photos_by_photographer(db, photographer)


@api.get("/photos/{photo_id}", response_model=schemas.photo.Photo)
def read_photo_by_id(photo_id: int, db: Session = Depends(get_db)):
    return crud.get_photo(db, photo_id)


@api.post("/photos/", response_model=schemas.photo.Photo)
def create_photo(photographer: str, db: Session = Depends(get_db)):
    db_photo = crud.create_photo(db, photo=schemas.photo.PhotoCreate(photographer=photographer))
    return db_photo
