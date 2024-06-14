""" Se esta utilizando la libreria simpy para manejar a los empleados
del deposito como recursos
 """

import simpy
import numpy as np

stock_auto_parte1 = 0
stock_auto_parte2 = 0
demanda = 0

class Deposito(object):
    def __init__(self, env, num_operarios):
        self.env = env
        self.operario = simpy.Resource(env, num_operarios)
        self.se_desocupa_operario = simpy.Store(env)
        self.ahora_no = env.event()

    def atender_requerimiento(self):
        global stock_auto_parte1
        global stock_auto_parte2
        global demanda
        if (stock_auto_parte1 > 0) & (stock_auto_parte2 > 0):
            stock_auto_parte1 -= 1
            stock_auto_parte2 -= 1
            demanda -= 1
            #aca van los tiempos exponenciales
            yield self.env.timeout(15)
        else:
            yield self.ahora_no

def solicitar_autopartes(env,deposito):
    with deposito.operario.request() as request:
        yield request
        """ print(f'{deposito.operario.count} of {deposito.operario.capacity} slots are allocated.') """
        yield env.process(deposito.atender_requerimiento())
        req = yield deposito.se_desocupa_operario.get()
        req.succeed()

def run_day(env,deposito):
    global demanda
    demandaDiaria = np.random.poisson(lam=56)
    demanda += demandaDiaria
    print(f'LLego demanda {demandaDiaria} y la total es {demanda}')
    for algo in range(deposito.operario.capacity):
        env.process(solicitar_autopartes(env,deposito))
    while demanda>1:
            req = env.event()
            deposito.se_desocupa_operario.put(req)
            yield req
            env.process(solicitar_autopartes(env,deposito))

def fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2):
    return stock_auto_parte1+120, stock_auto_parte2+150          

def main():
    horas_max = 12
    jornada_laboral = horas_max*60
    num_operarios_deposito = 2
    global stock_auto_parte1
    global stock_auto_parte2
    global demanda
  # Run the simulation
    for anio in range(3):
            for mes in range(12):
                for dia in range(30):
                    env = simpy.Environment()
                    deposito = Deposito(env, num_operarios_deposito)
                    if dia <= 15:
                        stock_auto_parte1, stock_auto_parte2 = fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2)
                    print(f'dia {dia}/{mes}/{anio} el stock es {stock_auto_parte1,stock_auto_parte2}')
                    env.process(run_day(env,deposito))
                    env.run(until=jornada_laboral)
                    print(f'La demanda quedo en {demanda}')

if __name__ == '__main__':
    main()
