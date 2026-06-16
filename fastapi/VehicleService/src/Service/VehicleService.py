from fastapi import HTTPException
from src.Repository.VehicleRepository import VehicleRepository

class VehicleService:

    def __init__(self):
        self.repository = VehicleRepository()

    def listar(self, id_usuario):
        vehiculos = self.repository.obtener_por_usuario(id_usuario)
        return vehiculos

    def registrar(self, vehicle, id_usuario):
        placa_existente = self.repository.buscar_por_placa(vehicle.placa)

        if placa_existente:
            raise HTTPException(
                status_code=400,
                detail="Ya existe un vehiculo con esa placa"
            )

        activos = self.repository.contar_activos(id_usuario)

        if activos >= 4:
            raise HTTPException(
                status_code=400,
                detail="Solo puede tener 4 vehiculos activos"
            )

        datos = {
            "idUsuario": id_usuario,
            "claveVehiculo": vehicle.claveVehiculo or vehicle.placa,
            "idModelo": vehicle.idModelo,
            "placa": vehicle.placa,
            "color": vehicle.color,
            "anio": vehicle.anio,
            "descripcion": vehicle.descripcion,
            "estatus": True
        }

        self.repository.guardar(datos)

        return {
            "success": True,
            "message": "Vehiculo registrado correctamente"
        }

    def actualizar(self, vehicle_id, vehicle, id_usuario):
        vehiculo = self.repository.obtener_por_id(vehicle_id)

        if not vehiculo:
            raise HTTPException(
                status_code=404,
                detail="Vehiculo no encontrado"
            )

        if vehiculo["idUsuario"] != id_usuario:
            raise HTTPException(
                status_code=403,
                detail="No tiene permisos para modificar este vehiculo"
            )

        placa_existente = self.repository.buscar_por_placa(vehicle.placa)

        if placa_existente and placa_existente["idVehiculo"] != vehicle_id:
            raise HTTPException(
                status_code=400,
                detail="La placa ya esta registrada"
            )

        datos = {
            "idModelo": vehicle.idModelo,
            "claveVehiculo": vehicle.claveVehiculo or vehicle.placa,
            "placa": vehicle.placa,
            "color": vehicle.color,
            "anio": vehicle.anio,
            "descripcion": vehicle.descripcion
        }

        self.repository.actualizar(vehicle_id, datos)

        return {
            "success": True,
            "message": "Vehiculo actualizado correctamente"
        }

    def cambiar_estatus(self, vehicle_id, estatus, id_usuario):
        vehiculo = self.repository.obtener_por_id(vehicle_id)

        if not vehiculo:
            raise HTTPException(
                status_code=404,
                detail="Vehiculo no encontrado"
            )

        if vehiculo["idUsuario"] != id_usuario:
            raise HTTPException(
                status_code=403,
                detail="No tiene permisos para modificar este vehiculo"
            )

        if estatus:
            activos = self.repository.contar_activos(id_usuario)

            if activos >= 4:
                raise HTTPException(
                    status_code=400,
                    detail="Solo puede tener 4 vehiculos activos"
                )

        self.repository.actualizar_estatus(
            vehicle_id,
            estatus
        )

        return {
            "success": True,
            "message": "Estatus actualizado correctamente"
        }
