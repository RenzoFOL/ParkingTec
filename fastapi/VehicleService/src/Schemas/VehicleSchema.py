from pydantic import BaseModel, Field

class VehicleCreate(BaseModel):

    idModelo: int
    placa: str = Field(min_length=5,max_length=10)
    color: str = Field(min_length=2,max_length=30)
    año: int
    descripcion: str = Field(max_length=200)
    estatus: bool = True

class VehicleUpdate(BaseModel):

    idModelo: int
    placa: str = Field(min_length=5,max_length=10)
    color: str = Field(min_length=2,max_length=30)
    año: int
    descripcion: str = Field(max_length=200)

class VehicleStatusUpdate(BaseModel):

    estatus: bool

from pydantic import BaseModel

class VehicleResponse(BaseModel):

    idVehiculo: int
    idUsuario: int
    idModelo: int
    modelo: str
    idMarca: int
    marca: str
    placa: str
    color: str
    año: int
    descripcion: str
    estatus: bool