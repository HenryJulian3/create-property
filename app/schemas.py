from pydantic import BaseModel
from typing import Optional

class PropertyCreate(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    price: float
