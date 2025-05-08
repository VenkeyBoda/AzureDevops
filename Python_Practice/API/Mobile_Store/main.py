from fastapi import FastAPI, HTTPException
from typing import List
from models import Mobile

app = FastAPI()

# In-memory database
mobiles_db: List[Mobile] = []

# Add a new mobile
@app.post("/mobiles/", response_model=Mobile)
def add_mobile(mobile: Mobile):
    for m in mobiles_db:
        if m.id == mobile.id:
            raise HTTPException(status_code=400, detail="Mobile with this ID already exists.")
    mobiles_db.append(mobile)
    return mobile

# List all mobiles
@app.get("/mobiles/", response_model=List[Mobile])
def list_mobiles():
    return mobiles_db

# Get a mobile by ID
@app.get("/mobiles/{mobile_id}", response_model=Mobile)
def get_mobile(mobile_id: int):
    for mobile in mobiles_db:
        if mobile.id == mobile_id:
            return mobile
    raise HTTPException(status_code=404, detail="Mobile not found.")

# "Buy" a mobile
@app.post("/mobiles/{mobile_id}/buy")
def buy_mobile(mobile_id: int, quantity: int = 1):
    for mobile in mobiles_db:
        if mobile.id == mobile_id:
            if mobile.in_stock >= quantity:
                mobile.in_stock -= quantity
                return {"message": f"Purchased {quantity} unit(s) of {mobile.brand} {mobile.model}."}
            else:
                raise HTTPException(status_code=400, detail="Not enough stock.")
    raise HTTPException(status_code=404, detail="Mobile not found.")
