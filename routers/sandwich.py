from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal

router = APIRouter(prefix="/sandwich", tags=["Sandwich"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Sandwich)
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return crud.create_sandwich(db, sandwich)

@router.get("/", response_model=list[schemas.Sandwich])
def read_sandwiches(db: Session = Depends(get_db)):
    return crud.get_sandwiches(db)

@router.get("/{sandwich_id}", response_model=schemas.Sandwich)
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = crud.get_sandwich(db, sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich

@router.put("/{sandwich_id}", response_model=schemas.Sandwich)
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return crud.update_sandwich(db, sandwich_id, sandwich)

@router.delete("/{sandwich_id}")
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return crud.delete_sandwich(db, sandwich_id)
