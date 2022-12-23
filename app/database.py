from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import time
# import psycopg2
# from psycopg2.extras import RealDictCursor

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1111@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# create session to connect to db and close it after (from sqlalchemy's official page)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# to use SQL
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1111',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('database connection was successful')
#         break
#     except Exception as error:
#         print(error)
#         time.sleep(2)
