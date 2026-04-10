from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import redis
import json

app = FastAPI(title="SIMAF API")

# =========================
# CONEXIÓN A REDIS
# =========================
r = redis.Redis(host="redis", port=6379, decode_responses=True)

# =========================
# "BASE DE DATOS" EN MEMORIA
# =========================
ingresos = []
egresos = []

# =========================
# MODELOS
# =========================
class Ingreso(BaseModel):
    id: int
    monto: float
    descripcion: str


class Egreso(BaseModel):
    id: int
    monto: float
    estado: str = "pendiente"


# =========================
# HOME
# =========================
@app.get("/")
def home():
    return RedirectResponse(url="/docs")


# =========================
# INGRESOS
# =========================
@app.post("/ingresos")
def crear_ingreso(ingreso: Ingreso):
    ingresos.append(ingreso)
    return {"mensaje": "Ingreso registrado"}


# =========================
# EGRESOS (CREATE)
# =========================
@app.post("/egresos")
def crear_egreso(egreso: Egreso):
    egresos.append(egreso)
    return {"mensaje": "Egreso registrado"}


# =========================
# APROBAR EGRESO
# =========================
@app.put("/egresos/{id}/aprobar")
def aprobar_egreso(id: int):
    for e in egresos:
        if e.id == id:
            e.estado = "aprobado"
            return {"mensaje": "Egreso aprobado"}
    raise HTTPException(status_code=404, detail="Egreso no encontrado")


# =========================
# GET CON CACHE + TTL
# =========================
@app.get("/egresos/{id}")
def obtener_egreso(id: int):
    key = f"egreso:{id}"

    # 1. BUSCAR EN REDIS (CACHE HIT)
    cache = r.get(key)
    if cache:
        return {
            "source": "redis-cache",
            "data": json.loads(cache)
        }

    # 2. BUSCAR EN "DB" (CACHE MISS)
    for e in egresos:
        if e.id == id:

            # 3. GUARDAR EN REDIS CON TTL (60 segundos)
            r.setex(
                key,
                60,  # TTL en segundos
                e.model_dump_json()
            )

            return {
                "source": "database",
                "data": e
            }

    raise HTTPException(status_code=404, detail="Egreso no encontrado")
