

def calc_rendimento():

    resultado = "Após {} período(s), o montante será de R${}"
    aporte_inicial = float(input("Valor inicial: R$"))
    rendimento_periodo = float(input("Rendimento por período (%): "))
    aporte_mensal = float(input("Aporte a cada período: R$"))
    total_periodos = int(input("Total de períodos: "))

    for i in range(total_periodos):
        aporte_inicial = calc_juros_compostos(aporte_inicial, rendimento_periodo, aporte_mensal)
        print(resultado.format(i+1,  str('%.2f' % aporte_inicial).replace('.', ',')))


def calc_juros_compostos(aporte_inicial, rendimento_periodo, aporte_mensal):
    return (aporte_inicial + (aporte_inicial * rendimento_periodo) / 100) + aporte_mensal


calc_rendimento()
