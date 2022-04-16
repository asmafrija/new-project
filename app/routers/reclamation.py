from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/reclamation",
    tags=['Reclamations']
)


@router.get("/", response_model=schemas.ReclamationsOut)
def get_my_reclamations(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0):
    my_reclamations = db.query(models.Reclamation).filter(models.Reclamation.owner_id == current_user.id).order_by(
        models.Reclamation.creation_date.desc()).limit(limit).offset(skip).all()
    return schemas.ReclamationsOut(list=[schemas.ReclamationOut(**rec.__dict__) for rec in my_reclamations],
                                   message="your reclamations",
                                   status=status.HTTP_200_OK)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReclamationOut)
def create_reclamation(reclamation: schemas.ReclamationCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_reclamation = models.Reclamation(
        owner_id=current_user.id, **reclamation.dict())
    db.add(new_reclamation)
    db.commit()
    db.refresh(new_reclamation)

    response = schemas.ReclamationOut(**new_reclamation.__dict__,
                                      status=status.HTTP_201_CREATED,
                                      message="Reclamation added successfully"
                                      )

    return response
