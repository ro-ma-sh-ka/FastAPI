from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(tags=['Authentication'])

# logic is:
# User send an email and a password
# API ask db is email exist
# if YES API compare passwords. BUT we store hashed password and we have to hash password user sent and after compare.
# we use method verify from utils to hash user password


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    # OAuth2PasswordRequestForm return 'username' and 'password'
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    # OAuth2PasswordRequestForm return 'username' and 'password'
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    # create a token
    access_token = oauth2.create_access_token(data={'user_id': user.id})

    return {'access_token': access_token, "token_type": 'Bearer'}
