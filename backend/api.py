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

    unidades_totales_por_mes, stock_auto_parte1_por_mes, stock_auto_parte2_por_mes, porcentaje_tiempo_sin_stock_por_año, promedio_tiempo_espera_por_mes = (
        simular(
            cantidad_operarios,
            dias_produccion,
            produccion_diaria_autoparte1,
            produccion_diaria_autoparte2,
        )
    )

    response = {
        "unidades_totales_por_mes": unidades_totales_por_mes,
        "stock_auto_parte1_por_mes": stock_auto_parte1_por_mes,
        "stock_auto_parte2_por_mes": stock_auto_parte2_por_mes,
        "porcentaje_tiempo_sin_stock_por_año": porcentaje_tiempo_sin_stock_por_año,
        "promedio_tiempo_espera_por_mes": promedio_tiempo_espera_por_mes,
    }

    print("----- Simulación realizada con éxito -----")
    print(response)

    return response

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

@app.post("/mock")
def read_root(simulacion: Simulacion):

    return {
        "unidades_totales_por_mes": [
            1076,
            1121,
            1101,
            1073,
            1112,
            1103,
            1082,
            1119,
            1011,
            1080,
            1080,
            1137
        ],
        "stock_auto_parte1_por_mes": [
            104,
            162,
            240,
            347,
            414,
            491,
            588,
            648,
            819,
            918,
            1018,
            1060
        ],
        "stock_auto_parte2_por_mes": [
            1094,
            2142,
            3210,
            4307,
            5364,
            6431,
            7518,
            8568,
            9729,
            10818,
            11908,
            12940
        ],
        "porcentaje_tiempo_sin_stock_por_año": [
            0.0, 3.2, 10
        ],
        "promedio_tiempo_espera_por_mes": [
            10832.080470603909,
            31240.831670411757,
            52674.016848781604,
            73916.41747539777,
            94061.37433726861,
            115365.70531048276,
            136176.73454805755,
            156114.9609369314,
            176807.35481143877,
            197483.74866889988,
            218495.47416145305,
            239722.9359322509
        ]
    }
