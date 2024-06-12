from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RideBase, RideDisplay, RideSearch
from models import Ride, User
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
    user = db.query(User).filter(User.id == ride.user_id).first()
    ride_data = ride.__dict__
    ride_data["username"] = user.username if user else "Unknown"
    return ride_data

@router.get("/", response_model=List[RideDisplay])
def get_all_rides(db: Session = Depends(get_db)):
    rides = db.query(Ride).all()
    rides_with_users = []
    for ride in rides:
        user = db.query(User).filter(User.id == ride.user_id).first()
        ride_data = ride.__dict__
        ride_data["username"] = user.username if user else "Unknown"
        rides_with_users.append(ride_data)
    return rides_with_users

@router.post("/search", response_model=List[RideDisplay])
def search_rides(request: RideSearch, db: Session = Depends(get_db)):
    rides = db.query(Ride).filter(
        Ride.departure == request.departure,
        Ride.destination == request.destination,
        Ride.date == request.date
    ).all()
    rides_with_users = []
    for ride in rides:
        user = db.query(User).filter(User.id == ride.user_id).first()
        ride_data = ride.__dict__
        ride_data["username"] = user.username if user else "Unknown"
        rides_with_users.append(ride_data)
    return rides_with_users
