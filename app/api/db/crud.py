from sqlalchemy.orm import Session

from . import models
from schemas.photo import PhotoCreate


def get_photo(db: Session, photo_id: int):
    return db.query(models.Photo).filter(models.Photo.id == photo_id).first()


def get_photos_by_photographer(db: Session, photographer: str):
    return db.query(models.Photo).filter(models.Photo.photographer == photographer).all()


def get_photos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Photo).offset(skip).limit(limit).all()


def create_photo(db: Session, photo: PhotoCreate):
    db_photo = models.Photo(
        file_path=photo.file_path, 
        width=photo.width, 
        height=photo.height,
        photographer=photo.photographer,
        taken_time=photo.taken_time)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo