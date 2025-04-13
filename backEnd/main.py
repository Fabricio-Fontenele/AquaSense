from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Recomendado: ["http://localhost:8080"] em dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados
class PayloadItem(BaseModel):
    id: int
    consumo: float
    DateTime: str
    idCliente: int

class PayloadData(BaseModel):
    payLoad: List[PayloadItem]

# Caminho para o arquivo JSON
json_file_path = "simulacao_consumo_agua_realista.json"

# Função para carregar o JSON do arquivo
def load_json_data():
    if not os.path.exists(json_file_path):
        raise HTTPException(status_code=404, detail="Arquivo JSON não encontrado")

    with open(json_file_path, "r") as f:
        data = json.load(f)
    
    return data["payLoad"]

# Endpoint para consultar os dados
@app.get("/payload")
def get_payload():
    try:
        payload = load_json_data()
        return {"payLoad": payload}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/consumo_diario")

def get_consumo():
    try:
        payload = load_json_data()
        # Se 'payload' for uma lista, basta iterar diretamente
        consumo_total = sum(item.get("consumo", 0) for item in payload)
        return {"consumo_total": consumo_total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
