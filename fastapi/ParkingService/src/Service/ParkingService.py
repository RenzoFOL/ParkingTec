import requests
from src.Repository.ParkingRepository import ParkingRepository
from src.Schemas.ParkingSchema import EntradaVehiculo
from datetime import datetime, timezone
import math

class ParkingService:
    def __init__(self):
        self.repository = ParkingRepository()

    def listar_cajones_libres(self):
        try:
            cajones = self.repository.obtener_cajones_libres()
            
            if not cajones:
                return []
                
            return cajones
        except Exception as e:
            return {"error": f"Error al consultar los espacios disponibles: {str(e)}"}
    
    def registrar_entrada_vehiculo(self, vehiculo: EntradaVehiculo, token: str):

        try:
            token_limpio = token.replace("Bearer ", "") if token.startswith("Bearer ") else token            
            headers_java = {
                "Authorization": f"Bearer {token_limpio}",
                "Accept": "application/json"
            }
            
            url_user = "http://127.0.0.1:8080/users/profile"
            resp_user = requests.get(url_user, headers=headers_java)

            if resp_user.status_code == 500:
                headers_java["Authorization"] = token_limpio
                resp_user = requests.get(url_user, headers=headers_java)
            
            if resp_user.status_code != 200:
                return {"error": f"Validación fallida: El UserService de Java rechazó la solicitud (Código {resp_user.status_code})."}
                
            usuario_data = resp_user.json()
            
            if usuario_data.get("claveUsuario") != vehiculo.claveUsuario:
                 return {"error": "Validación fallida: La clave de usuario enviada no coincide con el dueño del Token."}
                 
            if usuario_data.get("estatus") not in [1, True]:
                 return {"error": "Validación fallida: El usuario se encuentra inactivo en el sistema."}
                 
        except Exception as e:
            return {"error": f"Fallo de arquitectura de red: No se pudo conectar con UserService (Java)."}

        ids_vehiculos_usuario = []
        id_vehiculo_ingresando = None
        headers_python = {"Authorization": token}
        
        try:
            url_vehicles = "http://127.0.0.1:8000/vehicles/list"
            resp_veh = requests.get(url_vehicles, headers=headers_python) 
                        
            if resp_veh.status_code == 200:
                vehiculos = resp_veh.json()
                
                
                if isinstance(vehiculos, list):
                    for v in vehiculos:
                        if v.get("idUsuario") == usuario_data.get("idUsuario"):
                            ids_vehiculos_usuario.append(v.get("idVehiculo"))
                            
                            if v.get("placa") == vehiculo.placa:
                                id_vehiculo_ingresando = v.get("idVehiculo")
                        
                if not id_vehiculo_ingresando:
                    return {"error": "Validación fallida: La placa no existe, está inactiva o no te pertenece."}
            else:
                return {"error": f"El VehicleService respondió con un código de error {resp_veh.status_code}."}
        except Exception as e:
            return {"error": "Fallo de arquitectura: No se pudo conectar con VehicleService."}

        autos_adentro = self.repository.contar_autos_adentro(ids_vehiculos_usuario)
        if autos_adentro >= 2:
            return {"error": "Validación fallida: Ya alcanzaste el límite de 2 vehículos adentro."}

        return self.repository.registrar_entrada(id_vehiculo_ingresando)
    
    def registrar_salida_vehiculo(self, vehiculo: EntradaVehiculo, token: str):

        try:
            token_limpio = token.replace("Bearer ", "") if token.startswith("Bearer ") else token            
            headers_java = {
                "Authorization": f"Bearer {token_limpio}",
                "Accept": "application/json"
            }
            url_user = "http://127.0.0.1:8080/users/profile"
            resp_user = requests.get(url_user, headers=headers_java)

            if resp_user.status_code == 500:
                headers_java["Authorization"] = token_limpio
                resp_user = requests.get(url_user, headers=headers_java)
            
            if resp_user.status_code != 200:
                return {"error": f"Validación fallida: El UserService de Java rechazó la solicitud (Código {resp_user.status_code})."}
                
            usuario_data = resp_user.json()
            
            if usuario_data.get("claveUsuario") != vehiculo.claveUsuario:
                 return {"error": "Validación fallida: La clave de usuario enviada no coincide con el dueño del Token."}
                 
            if usuario_data.get("estatus") not in [1, True]:
                 return {"error": "Validación fallida: El usuario se encuentra inactivo en el sistema."}
                 
        except Exception:
            return {"error": "Fallo de arquitectura de red: No se pudo conectar con UserService (Java)."}

        id_vehiculo_valido = None
        headers_python = {"Authorization": token}
        
        try:
            url_vehicles = "http://127.0.0.1:8000/vehicles/list"
            resp_veh = requests.get(url_vehicles, headers=headers_python) 
                        
            if resp_veh.status_code == 200:
                vehiculos = resp_veh.json()
                if isinstance(vehiculos, list):
                    for v in vehiculos:
                        if v.get("idUsuario") == usuario_data.get("idUsuario"):
                            if v.get("placa") == vehiculo.placa:
                                id_vehiculo_valido = v.get("idVehiculo")
                        
                if not id_vehiculo_valido:
                    return {"error": "Validación fallida: La placa no existe, está inactiva o no te pertenece."}
            else:
                return {"error": f"El VehicleService respondió con un código de error {resp_veh.status_code}."}
        except Exception:
            return {"error": "Fallo de arquitectura: No se pudo conectar con VehicleService."}

        try:
            resultado = self.repository.registrar_salida(id_vehiculo_valido)
            
            if not resultado:
                return {"error": "Validación fallida: Este vehículo no cuenta con un registro de entrada activo."}
                
            return resultado
            
        except Exception as e:
            return {"error": f"Error en la base de datos local al registrar la salida: {str(e)}"}