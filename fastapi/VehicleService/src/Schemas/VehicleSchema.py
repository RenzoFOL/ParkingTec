from pydantic import BaseModel, Field

class VehicleCreate(BaseModel):
    claveVehiculo: str | None = Field(default=None, max_length=10)
    idModelo: int
    placa: str = Field(min_length=5, max_length=7)
    color: str = Field(min_length=2, max_length=20)
    anio: int
    descripcion: str | None = Field(default=None, max_length=255)

class VehicleUpdate(BaseModel):
    claveVehiculo: str | None = Field(default=None, max_length=10)
    idModelo: int
    placa: str = Field(min_length=5, max_length=7)
    color: str = Field(min_length=2, max_length=20)
    anio: int
    descripcion: str | None = Field(default=None, max_length=255)

class VehicleStatusUpdate(BaseModel):
    estatus: bool

class VehicleResponse(BaseModel):
    idVehiculo: int
    idUsuario: int
    claveVehiculo: str
    idMarca: int
    marca: str
    idModelo: int
    modelo: str
    placa: str
    color: str
    anio: int
    descripcion: str | None