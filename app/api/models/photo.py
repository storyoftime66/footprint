from pydantic import BaseModel
from datetime import datetime


class Photo(BaseModel):
    file_name: str = ""
    extension: str = ""
    file_format: str = ""
    height: int = 0
    width: int = 0

    photographer: str = ""
    taken_time: datetime = datetime.now()
    longitude: float = 0.0
    latitude: float = 0.0
    altitude: float = 0.0
