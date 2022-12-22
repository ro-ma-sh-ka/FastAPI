# use passlib to hash password
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


# we hash password user send when create an account
def hash(password: str):
    return pwd_context.hash(password)


# we hash password user send to login into his account
# and return to method where we compare saved password and sent password
def verify(plain_password: str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
