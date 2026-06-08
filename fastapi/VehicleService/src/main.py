from fastapi import FastAPI
from src.Controller.VehicleController import router_vehicle

app = FastAPI()

app.include_router(prefix="vehicles", router=router_vehicle)