from pydantic import BaseModel, Field, field_validator

class VehicleCreate(BaseModel):
    claveVehiculo: str | None = Field(default=None, max_length=10)
    idModelo: int
    placa: str
    color: str
    anio: int
    descripcion: str

    @field_validator("idModelo")
    @classmethod
    def validar_modelo(cls, value):
        if value <= 0:
            raise ValueError("Debe seleccionar un modelo válido")
        return value
    
    @field_validator("placa")
    @classmethod
    def validar_placa(cls, value):
        if not value or not value.strip():
            raise ValueError("La placa no puede estar vacía")
        value = value.strip().upper()
        if len(value) < 5:
            raise ValueError("La placa debe tener al menos 5 caracteres")
        if len(value) > 7:
            raise ValueError("La placa no puede tener más de 7 caracteres")
        return value

    @field_validator("color")
    @classmethod
    def validar_color(cls, value):
        if not value or not value.strip():
            raise ValueError("El color no puede estar vacío")
        value = value.strip()
        if len(value) < 2:
            raise ValueError("El color debe tener al menos 2 caracteres")
        if len(value) > 20:
            raise ValueError("El color no puede tener más de 20 caracteres")
        return value

    @field_validator("anio")
    @classmethod
    def validar_anio(cls, value):
        if value < 1900:
            raise ValueError("El año no puede ser menor a 1900")
        if value > 2100:
            raise ValueError("El año no puede ser mayor a 2100")
        return value
    
    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, value):
        if not value or not value.strip():
            raise ValueError("La descripción no puede estar vacía")
        value = value.strip()
        if len(value) < 5:
            raise ValueError("La descripción debe tener al menos 5 caracteres")
        if len(value) > 255:
            raise ValueError("La descripción no puede tener más de 255 caracteres")
        return value

class VehicleUpdate(VehicleCreate):
    pass

class VehicleStatusUpdate(BaseModel):
    estatus: bool

    @field_validator("estatus", mode="before")
    @classmethod
    def validar_estatus(cls, value):
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError("El estatus es obligatorio y no puede estar vacío")

        if isinstance(value, int):
            if value not in (0, 1):
                raise ValueError("El estatus solo puede ser 0 o 1")
            return bool(value)

        if isinstance(value, bool):
            return value

        raise ValueError("El estatus solo puede ser true/false o 0/1")
    
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
    estatus: bool