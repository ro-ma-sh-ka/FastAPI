from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2

router = APIRouter(prefix='/vote', tags=['Vote'])


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user {current_user.id}'
                                                                             f'has already voted post {vote.post_id}')
        new_vote = models.Vote(user_id = current_user.id, post_id=vote.post_id)
        db.add(new_vote)
        db.commit()
        return {'message': 'successfully added vote'}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vote does not found')
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {'message': 'successfully deleted vote'}