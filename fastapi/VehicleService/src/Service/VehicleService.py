# Service/VehicleService.py

from fastapi import HTTPException
from Repository.VehicleRepository import VehicleRepository

class VehicleService:

    def __init__(self):
        self.repository = VehicleRepository()

    def listar(self, id_usuario):
        vehiculos = self.repository.obtener_por_usuario(id_usuario)
        return vehiculos

    def registrar(self, vehicle, id_usuario):
        #Por placa no puede haber dos vehículos registrados
        placa_existente = (self.repository.buscar_por_placa(vehicle.placa))
        if placa_existente:
            raise HTTPException(
                status_code=400,
                detail="Ya existe un vehículo con esa placa"
            )

        # Un usuario no puede tener más de 4 vehículos activos
        activos = (self.repository.contar_activos(id_usuario))
        if activos >= 4:
            raise HTTPException(
                status_code=400,
                detail="Solo puede tener 4 vehículos activos"
            )

        # Registrar vehículo
        datos = {
            "idUsuario": id_usuario,
            "idModelo": vehicle.idModelo,
            "placa": vehicle.placa,
            "color": vehicle.color,
            "año": vehicle.año,
            "descripcion": vehicle.descripcion,
            "estatus": vehicle.estatus
            }
        self.repository.guardar(datos)

        return {
            "success": True,
            "message": "Vehículo registrado correctamente"
        }

    def actualizar(self, vehicle_id, vehicle, id_usuario):
        vehiculo = (self.repository.obtener_por_id(vehicle_id))

        if not vehiculo:
            raise HTTPException(
                status_code=404,
                detail="Vehículo no encontrado"
            )

        # Validar propietario
        if vehiculo["idUsuario"] != id_usuario:
            raise HTTPException(
                status_code=403,
                detail="No tiene permisos para modificar este vehículo"
            )

        # Validar placa repetida
        placa_existente = (self.repository.buscar_por_placa(vehicle.placa))

        if (placa_existente and placa_existente["idVehiculo"] != vehicle_id):
            raise HTTPException(
                status_code=400,
                detail="La placa ya está registrada"
            )

        datos = {
            "idModelo": vehicle.idModelo,
            "placa": vehicle.placa,
            "color": vehicle.color,
            "anio": vehicle.anio,
            "descripcion": vehicle.descripcion
        }

        self.repository.actualizar(vehicle_id,datos)

        return {
            "success": True,
            "message": "Vehículo actualizado correctamente"
        }

    def cambiar_estatus(self, vehicle_id, estatus, id_usuario):
        vehiculo = (self.repository.obtener_por_id(vehicle_id))

        if not vehiculo:
            raise HTTPException(
                status_code=404,
                detail="Vehículo no encontrado"
            )

        # Validar propietario
        if vehiculo["idUsuario"] != id_usuario:
            raise HTTPException(
                status_code=403,
                detail="No tiene permisos para modificar este vehículo"
            )

        self.repository.actualizar_estatus(vehicle_id, estatus)

        return {
            "success": True,
            "message": "Estatus actualizado correctamente"
        }