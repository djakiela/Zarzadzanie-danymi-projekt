from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RideBase, RideDisplay, RideSearch
from models import Ride
from database import get_db
from typing import List

router = APIRouter(prefix="/ride", tags=["ride"])

@router.post("/", response_model=RideDisplay)
def create_ride(request: RideBase, db: Session = Depends(get_db)):
    new_ride = Ride(
        departure=request.departure,
        destination=request.destination,
        date=request.date,
        time=request.time,
        passengers=request.passengers,
        phone_number=request.phone_number,
        user_id=request.user_id
    )
    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)
    return new_ride

@router.get("/{id}", response_model=RideDisplay)
def get_ride(id: int, db: Session = Depends(get_db)):
    ride = db.query(Ride).filter(Ride.id == id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return ride

@router.get("/", response_model=List[RideDisplay])
def get_all_rides(db: Session = Depends(get_db)):
    rides = db.query(Ride).all()
    return rides

@router.post("/search", response_model=List[RideDisplay])
def search_rides(request: RideSearch, db: Session = Depends(get_db)):
    rides = db.query(Ride).filter(
        Ride.departure == request.departure,
        Ride.destination == request.destination,
        Ride.date == request.date
    ).all()
    return rides
