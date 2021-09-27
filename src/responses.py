#Módulo para uso do FastAPI (apenas para teste)
from pydantic import BaseModel

class TrendItem(BaseModel):
    name: str
    url: str
