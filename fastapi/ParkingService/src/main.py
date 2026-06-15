from fastapi import FastAPI
from src.Controller.ParkingController import router_parking

app = FastAPI()

app.include_router(router_parking, prefix="/parking")