from fastapi import FastAPI
from pydantic import BaseModel
from simulacion import simular
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras
)


class Simulacion(BaseModel):
    cantidad_operarios: int
    dias_produccion: int
    produccion_diaria_autoparte1: int
    produccion_diaria_autoparte2: int


@app.get("/status")
def status():
    return {"status": "ok"}


@app.post("/simular")
def read_root(simulacion: Simulacion):

    cantidad_operarios = simulacion.cantidad_operarios
    dias_produccion = simulacion.dias_produccion
    produccion_diaria_autoparte1 = simulacion.produccion_diaria_autoparte1
    produccion_diaria_autoparte2 = simulacion.produccion_diaria_autoparte2

    unidades_totales_por_mes, stock_auto_parte1_por_mes, stock_auto_parte2_por_mes = (
        simular(
            cantidad_operarios,
            dias_produccion,
            produccion_diaria_autoparte1,
            produccion_diaria_autoparte2,
        )
    )

    return {
        "unidades_totales_por_mes": unidades_totales_por_mes,
        "stock_auto_parte1_por_mes": stock_auto_parte1_por_mes,
        "stock_auto_parte2_por_mes": stock_auto_parte2_por_mes,
    }

import random

@app.post("/random")
def read_root(simulacion: Simulacion):
    unidades_totales_por_mes = [random.randint(50000, 70000)]
    stock_auto_parte1_por_mes = [random.randint(1000, 2500)]
    stock_auto_parte2_por_mes = [random.randint(1000, 15000)]

    for _ in range(35): 
        unidades_totales_por_mes.append(unidades_totales_por_mes[-1] + random.randint(100, 500))
        stock_auto_parte1_por_mes.append(stock_auto_parte1_por_mes[-1] + random.randint(50, 200))
        stock_auto_parte2_por_mes.append(stock_auto_parte2_por_mes[-1] + random.randint(200, 1000))

    return {
        "unidades_totales_por_mes": unidades_totales_por_mes,
        "stock_auto_parte1_por_mes": stock_auto_parte1_por_mes,
        "stock_auto_parte2_por_mes": stock_auto_parte2_por_mes
    }
