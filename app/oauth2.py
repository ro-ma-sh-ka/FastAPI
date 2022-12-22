from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


# logic of token creation:
# we create a token which include:
#  - header (algorithm, type - we use jose library),
#  - payload data (email, name, user_id, etc.),
#  - signature (which contain SECRET_KEY, payload, header)
# API receipt token and compare signature with a test signature. If it doesn't match no access

# SECRET_KEY - for our token
# Algorithm
# Expiration time - how long user can be logined


SECRET_KEY = '1we324wqfew5grvsd5tvgrsdw45e2341frewvfwr3421rfre4f4deq4rdrq4rf245g3h6g75unj'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    # create a copy of data dictionary not to change original dict
    to_encode = data.copy()
    # calculate time when user must be logout
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # add this time to our copy of dict
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return  token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'could not validate',
                                          headers={'WWW-Authenticate': 'Bearer'})
    return verify_access_token(token, credentials_exception)
