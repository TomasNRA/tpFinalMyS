import numpy as np

def fabricarAutoPartes(stock_autoparte1,stock_autoparte2):
    return stock_autoparte1+120, stock_autoparte2+150

def atenderPedido(stock_auto_parte1,stock_auto_parte2, demanda_pendiente):
    horas_max = 12
    jornada_laboral = horas_max*60
    new_stock_auto_parte1 = stock_auto_parte1
    new_stock_auto_parte2 = stock_auto_parte2
    new_demanda_pendiente = demanda_pendiente

    while True:
        if new_stock_auto_parte1>0 and new_stock_auto_parte2>0 and new_demanda_pendiente>0:
            new_stock_auto_parte1 -= 1
            new_stock_auto_parte2 -= 1
            new_demanda_pendiente -= 1
            jornada_laboral -= 15
        if jornada_laboral == 0:
            break
    return new_stock_auto_parte1,new_stock_auto_parte2, new_demanda_pendiente

def main():
    stock_auto_parte1 = 0
    stock_auto_parte2 = 0
    demanda_pendiente = 0
    for anio in range(3):
        for mes in range(12):
            for dia in range(30):
                if dia <= 15:
                    stock_auto_parte1, stock_auto_parte2 = fabricarAutoPartes(stock_auto_parte1,stock_auto_parte2)
                print(f'dia {dia}/{mes}/{anio} el stock es {stock_auto_parte1,stock_auto_parte2}')
                demanda = np.random.poisson(lam=56)
                demanda_pendiente += demanda
                print(f'LLego demanda {demanda}, y la total es {demanda_pendiente}')
                stock_auto_parte1, stock_auto_parte2,demanda_pendiente = atenderPedido(stock_auto_parte1, stock_auto_parte2,demanda_pendiente)
                print(f'La demanda quedo en {demanda_pendiente}')
        

if __name__ == "__main__":
    main()