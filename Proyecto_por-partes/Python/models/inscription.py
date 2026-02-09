from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class InscriptionModel(BaseModel):
    id_alumno: str
    id_excursion: str
    estado_pago: str = "pendiente"
    fecha_inscripcion: datetime = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
            "example": {
                "id_alumno": "65c8f...",
                "id_excursion": "65c9a...",
                "estado_pago": "pagado"
            }
        }