from fastapi import FastAPI
from pydantic import BaseModel
from EventosDiscretos.tpFinal import simular

app = FastAPI()

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

    unidades_totales_por_mes, stock_auto_parte1_por_mes, stock_auto_parte2_por_mes = simular(cantidad_operarios, dias_produccion, produccion_diaria_autoparte1, produccion_diaria_autoparte2)

    return {
        "unidades_totales_por_mes": unidades_totales_por_mes, 
        "stock_auto_parte1_por_mes": stock_auto_parte1_por_mes, 
        "stock_auto_parte2_por_mes": stock_auto_parte2_por_mes
    }