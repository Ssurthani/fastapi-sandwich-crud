from sqlalchemy.orm import Session
from models import Sandwich
from schemas import SandwichCreate

def get_sandwich(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

def get_sandwiches(db: Session):
    return db.query(Sandwich).all()

def create_sandwich(db: Session, sandwich: SandwichCreate):
    db_sandwich = Sandwich(name=sandwich.name, ingredients=sandwich.ingredients)
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def update_sandwich(db: Session, sandwich_id: int, sandwich: SandwichCreate):
    db_sandwich = get_sandwich(db, sandwich_id)
    if db_sandwich:
        db_sandwich.name = sandwich.name
        db_sandwich.ingredients = sandwich.ingredients
        db.commit()
        db.refresh(db_sandwich)
    return db_sandwich

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = get_sandwich(db, sandwich_id)
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
    return db_sandwich
