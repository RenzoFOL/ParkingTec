from fastapi import APIRouter, Depends
from Middleware.Jwt import validate_token

from Schemas.VehicleSchema import *
from Service.VehicleService import VehicleService

router_vehicle = APIRouter() 

##Endpoints para registrar, listar, actualizar y cambiar el estado de los vehículos
@router_vehicle.post("/register")
def register_vehicle(vehicle: VehicleCreate,  user = Depends(validate_token)):
    return VehicleService.registrar(vehicle, user["idUsuario"])

@router_vehicle.get("/list")
def list_vehicles(user = Depends(validate_token)):
    return VehicleService.listar(user["idUsuario"])

@router_vehicle.put("/update/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: VehicleUpdate, user = Depends(validate_token)):
    return VehicleService.actualizar(vehicle_id, vehicle, user["idUsuario"])

@router_vehicle.patch("/update_status/{vehicle_id}")
def update_status(vehicle_id: int, body: VehicleStatusUpdate, user = Depends(validate_token)):
    return VehicleService.cambiar_estatus(vehicle_id, body.estatus, user["idUsuario"])