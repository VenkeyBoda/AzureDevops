from pydantic import BaseModel
from typing import Optional

class Mobile(BaseModel):
    id: int
    brand: str
    model: str
    price: float
    in_stock: int
    description: Optional[str] = None
