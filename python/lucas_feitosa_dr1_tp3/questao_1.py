
def divisao_conta():

    print("QUESTÃO 01")
    total_pessoas: int = 0
    total_consumo: float = 0.0
    percentual_servico: float = 0.0
    resultado = 0
    mensagem_erro = 'Valor Inválido'
    mensagem_sucesso = 'Dividindo a conta por {0} pessoa(s), cada pessoa deverá pagar R$ {1}'

    print('Insira o total de pessoas: ')
    total_pessoas = int(input())

    if total_pessoas <= 0:
        print(mensagem_erro)
        return

    print('Insira o percentual de serviço entre 0 e 100: ')
    percentual_servico = float(input())

    if percentual_servico < 0 or percentual_servico > 100:
        print(mensagem_erro)
        return

    print('Insira o total do consumo: R$ ')
    total_consumo = float(input())

    if total_consumo < 0:
        print(mensagem_erro)
        return

    resultado = divide_conta(total_consumo, percentual_servico, total_pessoas)
    resultado = str('%.2f' % resultado).replace('.', ',')

    print(mensagem_sucesso.format(total_pessoas, resultado))


def divide_conta(total_consumo, percentual_servico, total_pessoas):
    return (total_consumo + percentual_servico) / total_pessoas

divisao_conta()
