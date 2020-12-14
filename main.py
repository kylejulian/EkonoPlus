from fastapi import  HTTPException
from fastapi import  FastAPI
import db

app = FastAPI()

@app.get("/registros/consultar/")
async def consultar_registros():
    registro = db.consultar_registro()
    return registro


@app.post("/registros/crear/")
async def crear_registro(dato: db.registro):
    registro_creado= db.crear_registro(dato)

    if registro_creado:
        return {"mensaje": "Registro creado"}
    else:
        raise HTTPException(status_code= 400, detail= "Orden ya existe")