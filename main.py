from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="SIMAF API")

ingresos = []
egresos = []

class Ingreso(BaseModel):
    id: int
    monto: float
    descripcion: str

class Egreso(BaseModel):
    id: int
    monto: float
    estado: str = "pendiente"

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

@app.post("/ingresos")
def crear_ingreso(ingreso: Ingreso):
    ingresos.append(ingreso)
    return {"mensaje": "Ingreso registrado"}

@app.post("/egresos")
def crear_egreso(egreso: Egreso):
    egresos.append(egreso)
    return {"mensaje": "Egreso registrado"}

@app.put("/egresos/{id}/aprobar")
def aprobar_egreso(id: int):
    for e in egresos:
        if e.id == id:
            e.estado = "aprobado"
            return {"mensaje": "Egreso aprobado"}
    raise HTTPException(status_code=404, detail="Egreso no encontrado")

@app.get("/egresos/{id}")
def obtener_egreso(id: int):
    for e in egresos:
        if e.id == id:
            return e
    raise HTTPException(status_code=404, detail="Egreso no encontrado")