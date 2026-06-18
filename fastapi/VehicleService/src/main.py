from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from json import JSONDecodeError

from src.Controller.VehicleController import router_vehicle

app = FastAPI()

app.include_router(
    router_vehicle,
    prefix="/vehicles"
)
