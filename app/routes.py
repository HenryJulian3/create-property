from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import Property
from .schemas import PropertyCreate

router = APIRouter()

@router.post("/create")
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    new_property = Property(**property.dict())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return {"message": "Property created successfully", "property": new_property}
