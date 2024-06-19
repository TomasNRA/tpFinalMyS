""" Se esta utilizando la libreria simpy para manejar a los empleados
del deposito como recursos
 """

import simpy
import numpy as np

stock_auto_parte1 = 0
stock_auto_parte2 = 0
demanda = 0
unidades_totales = 0

class Deposito(object):
    def __init__(self, env, num_operarios):
        self.env = env
        self.operario = simpy.Resource(env, num_operarios)
        self.no_hay_stock = env.event()

    def atender_requerimiento(self):
        global stock_auto_parte1
        global stock_auto_parte2
        global demanda
        if (stock_auto_parte1 > 0) and (stock_auto_parte2 > 0):
            stock_auto_parte1 -= 1
            stock_auto_parte2 -= 1
            demanda -= 1
            yield self.env.timeout(np.random.exponential(scale=8)+np.random.exponential(scale=12))
        else:
            print('me quede sin stock')
            yield self.no_hay_stock

def solicitar_autopartes(env,deposito):
    global unidades_totales
    with deposito.operario.request() as request:
        yield request
        yield env.process(deposito.atender_requerimiento())
        unidades_totales += 1

def run_day(env,deposito):
    global demanda
    print(f'Al comenzar el dia, la demanda es: {demanda}')

    #Si arranca el dia con demanda insatisfecha, se etiende 
    if demanda > 0:
        for algo in range(demanda):
            env.process(solicitar_autopartes(env,deposito))

    #Se va generando demanda con un tiempo entre llegadas con una distribucion exponencial
    while True:
        demanda +=1
        env.process(solicitar_autopartes(env,deposito))
        yield env.timeout(np.random.exponential(scale=1/0.0972)) #0.0972 sale de dividir 70 por la jornada laboral

def fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2, produccion_diaria_autoparte1, produccion_diaria_autoparte2):
    return stock_auto_parte1+produccion_diaria_autoparte1, stock_auto_parte2+produccion_diaria_autoparte2

def simular(cantidad_operarios=2, dias_produccion=15, produccion_diaria_autoparte1=120, produccion_diaria_autoparte2=150):
    horas_max = 12
    jornada_laboral = horas_max*60
    num_operarios_deposito = cantidad_operarios
    global stock_auto_parte1
    global stock_auto_parte2
    global demanda
    global unidades_totales

    for anio in range(3):
            for mes in range(12):
                for dia in range(30):
                    env = simpy.Environment()
                    deposito = Deposito(env, num_operarios_deposito)
                    if dia <= dias_produccion:
                        stock_auto_parte1, stock_auto_parte2 = fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2, produccion_diaria_autoparte1, produccion_diaria_autoparte2)
                    print(f'dia {dia}/{mes}/{anio} el stock es {stock_auto_parte1,stock_auto_parte2}')
                    env.process(run_day(env,deposito))
                    env.run(until=jornada_laboral)
                    print(f'La demanda quedo en {demanda}')
    print(f'{unidades_totales=}')

if __name__ == '__main__':
    simular()
