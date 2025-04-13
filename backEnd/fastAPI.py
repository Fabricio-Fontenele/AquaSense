from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# Estrutura do item individual
class PayloadItem(BaseModel):
    id: int
    consumo: float
    DateTime: str
    idCliente: int

# Estrutura do payload
class PayloadData(BaseModel):
    payLoad: List[PayloadItem]

# Armazenamento em memória
payload_storage: List[PayloadItem] = []

# Endpoint para upload do JSON
@app.post("/upload-json/")
async def upload_json(file: UploadFile = File(...)):
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um .json")

    contents = await file.read()
    try:
        data = json.loads(contents)
        payload = PayloadData(**data)  # Validação com Pydantic
        global payload_storage
        payload_storage = payload.payLoad
        return {"message": "Arquivo processado com sucesso", "total": len(payload_storage)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao processar JSON: {str(e)}")

# Endpoint para visualizar os dados
@app.get("/payload/")
def get_payload():
    return {"payLoad": payload_storage