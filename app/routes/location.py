from fastapi import APIRouter, HTTPException
from app.utils.geo import get_coordinates


router = APIRouter()

@router.get('/location')
async def get_location_data(city: str):
    data = await get_coordinates(city)
    if not data:
        raise HTTPException(status_code=404, detail="City not found.")
    return data
