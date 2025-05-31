import httpx


async def get_coordinates(city : str):
    url =  "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "IntelBoard/1.0"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        data = response.json()
        if data:
            return {
                "city": city,
                "lat": data[0]["lat"],
                "lon": data[0]["lon"]
            }
        else:
            return None

async def fetch_embassies(lat, lon, radius_km=5):
    overpass_url = "https://overpass-api.de/api/interpreter"
    bbox = f"{float(lat)-0.05},{float(lon)-0.05},{float(lat)+0.05},{float(lon)+0.05}"
    query = f"""
    [out:json];
    node["amenity"="embassy"]({bbox});
    out body;
    """
    async with httpx.AsyncClient() as client:
        res = await client.post(overpass_url, data=query, headers={"User-Agent": "IntelBoard"})
        return res.json()