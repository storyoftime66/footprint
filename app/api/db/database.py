import os
import yaml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB = {
    "dialect": "mysql",
    "driver": "pymysql",
    "host": "localhost:3307",
    "user": "root",
    "password": "root",
    "database": "footprint"
}
with open(os.path.abspath(os.path.join(os.path.abspath(__file__) + "/../../config.yml"))) as f:
    DB.update(list(yaml.safe_load_all(f))[0].get("db", {}))

URL = f"{DB['dialect']}+{DB['driver']}://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}"

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
