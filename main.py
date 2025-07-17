from fastapi import FastAPI
from pydantic import BaseModel
from db import get_connection

app = FastAPI()

class GeoData(BaseModel):
    name: str
    email: str
    lat: float
    lng: float
    category: str

@app.post("/submit")
def submit(data: GeoData):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO geo_data (name, email, lat, lng, category) VALUES (%s, %s, %s, %s, %s)",
        (data.name, data.email, data.lat, data.lng, data.category)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Data saved!"}
