from pydantic import BaseModel

class EspacioEstacionamiento(BaseModel):
    idEspacio:int
    claveEspacio:str
    tipo:str
    ocupado:int
    estatus:int

class EntradaVehiculo(BaseModel):
    claveUsuario:str
    placa:str