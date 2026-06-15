from fastapi import APIRouter, Depends, Request
from src.Service.ParkingService import ParkingService
from src.Schemas.ParkingSchema import EntradaVehiculo
from src.Middleware.Jwt import validate_token

router_parking = APIRouter()

@router_parking.get("/libres")
def get_cajones_libres(user = Depends(validate_token)):
    service = ParkingService()
    return service.listar_cajones_libres()

@router_parking.post("/entrada")
def registrar_entrada(body: EntradaVehiculo, request: Request, user = Depends(validate_token)):
    token = request.headers.get("Authorization")
    service = ParkingService()
    return service.registrar_entrada_vehiculo(body, token)

@router_parking.post("/salida")
def registrar_salida(body: EntradaVehiculo, request: Request, user = Depends(validate_token)):
    token = request.headers.get("Authorization")
    service = ParkingService()
    return service.registrar_salida_vehiculo(body, token)