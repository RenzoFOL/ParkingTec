from fastapi import APIRouter, Depends
from src.Middleware.Jwt import validate_token
from src.Schemas.VehicleSchema import VehicleCreate, VehicleStatusUpdate, VehicleUpdate
from src.Service.VehicleService import VehicleService

router_vehicle = APIRouter()

@router_vehicle.post("/register")
def register_vehicle(vehicle: VehicleCreate, user = Depends(validate_token)):
    service = VehicleService()
    return service.registrar(vehicle, user["idUsuario"])

@router_vehicle.get("/list")
def list_vehicles(user = Depends(validate_token)):
    service = VehicleService()
    return service.listar(user["idUsuario"])

@router_vehicle.put("/update/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: VehicleUpdate, user = Depends(validate_token)):
    service = VehicleService()
    return service.actualizar(vehicle_id, vehicle, user["idUsuario"])

@router_vehicle.patch("/update_status/{vehicle_id}")
def update_status(vehicle_id: int, body: VehicleStatusUpdate, user = Depends(validate_token)):
    service = VehicleService()
    return service.cambiar_estatus(vehicle_id, body.estatus, user["idUsuario"])
