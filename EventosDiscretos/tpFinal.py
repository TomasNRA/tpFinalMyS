""" Se esta utilizando la libreria simpy para manejar a los empleados
del deposito como recursos
 """

import simpy
import numpy as np
from queue import Queue
from datetime import date,timedelta
from dateutil.rrule import rrule, DAILY,YEARLY, MONTHLY
import calendar

stock_auto_parte1 = 0
stock_auto_parte2 = 0
demanda = Queue()
demanda_satisfecha_mensual = 0
tiempo_espera_mensual = 0
unidades_totales = 0

class Deposito(object):
    def __init__(self, env, num_operarios):
        self.env = env
        self.operario = simpy.Resource(env, num_operarios)
        self.no_hay_stock = env.event()

    def atender_requerimiento(self,tiempo_actual):
        global stock_auto_parte1
        global stock_auto_parte2
        global demanda
        global tiempo_espera_mensual
        if (stock_auto_parte1 > 0) and (stock_auto_parte2 > 0):
            stock_auto_parte1 -= 1
            stock_auto_parte2 -= 1
            tiempo_demanda = demanda.get()
            yield self.env.timeout(np.random.exponential(scale=8)+np.random.exponential(scale=12))
            tiempo_espera_mensual += ((tiempo_actual+timedelta(minutes=self.env.now)) - tiempo_demanda).total_seconds()/60
        else:
            print('me quede sin stock')
            yield self.no_hay_stock

def solicitar_autopartes(env,deposito,tiempo_actual):
    global unidades_totales
    global demanda_satisfecha_mensual
    
    with deposito.operario.request() as request:
        yield request
        yield env.process(deposito.atender_requerimiento(tiempo_actual))
        demanda_satisfecha_mensual += 1
        unidades_totales += 1

def run_day(env,deposito,fecha_actual):
    global demanda
    operario_max_pedidos = 50 #cantidad mayor al tope de pedidos que puede atender un operario

    print(f'Al comenzar el dia, la demanda es: {demanda.qsize()}')
    control = 0
    #Si arranca el dia con demanda insatisfecha, se atiende
    if demanda.qsize() > 0:
        for algo in range(demanda.qsize()):
            env.process(solicitar_autopartes(env,deposito,fecha_actual))
            control += 1
            if control >= operario_max_pedidos*deposito.operario.capacity:
                break

    #Se va generando demanda con un tiempo entre llegadas con una distribucion exponencial
    while True:
        demanda.put(fecha_actual+timedelta(minutes=env.now))
        env.process(solicitar_autopartes(env,deposito,fecha_actual))
        yield env.timeout(np.random.exponential(scale=1/0.0972)) #0.0972 sale de dividir 70 por la jornada laboral

def fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2):
    return stock_auto_parte1+200, stock_auto_parte2+100

def main():
    start_date = date(2024, 6, 1)
    horas_max = 12
    jornada_laboral = horas_max*60
    num_operarios_deposito = 1
    global stock_auto_parte1
    global stock_auto_parte2
    global demanda
    global unidades_totales
    global demanda_satisfecha_mensual
    global tiempo_espera_mensual

    unidades_totales_por_mes = []
    stock_auto_parte1_por_mes = []
    stock_auto_parte2_por_mes = []
    porcentaje_tiempo_sin_stock_por_año = []
    promedio_tiempo_espera_por_mes = []

    for anio in rrule(YEARLY,dtstart=start_date,count=3):
        dias_sin_stock = 0
        for mes in rrule(MONTHLY,dtstart=anio,count=12):
            demanda_satisfecha_mensual = 0
            tiempo_espera_mensual = 0
            unidades_totales = 0
            end_date = mes + timedelta(calendar.monthrange(mes.year,mes.month)[1]-1)
            for dia in rrule(DAILY,dtstart=mes,until=end_date):
                env = simpy.Environment()
                deposito = Deposito(env, num_operarios_deposito)
                if dia <= (mes+ timedelta(days=9)): ##parametrizar
                    stock_auto_parte1, stock_auto_parte2 = fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2)
                print(f'dia {dia} el stock es {stock_auto_parte1,stock_auto_parte2}')
                if stock_auto_parte1 and stock_auto_parte2 == 0:
                    dias_sin_stock += 1
                env.process(run_day(env,deposito,dia))
                env.run(until=jornada_laboral)
                print(f'La demanda quedo en {demanda.qsize()}')
            print(f'Tiempo de espera {tiempo_espera_mensual} y demanda satisfecha por mes {demanda_satisfecha_mensual}')
            print(f'Tiempo de espera mensual promedio {tiempo_espera_mensual/demanda_satisfecha_mensual} minutos')

            unidades_totales_por_mes.append(unidades_totales)
            stock_auto_parte1_por_mes.append(stock_auto_parte1)
            stock_auto_parte2_por_mes.append(stock_auto_parte2)
            promedio_tiempo_espera_por_mes.append(tiempo_espera_mensual/demanda_satisfecha_mensual) #esto esta expresado en minutos 
        print(f'Dias sin stock {dias_sin_stock}')
        porcentaje_tiempo_sin_stock_por_año.append(dias_sin_stock/3.65) #esto es un porcentaje anual
    print(f'{unidades_totales=}')

if __name__ == '__main__':
    main()
