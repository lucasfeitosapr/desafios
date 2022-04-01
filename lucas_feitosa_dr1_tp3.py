
def divisao_conta():

    print("QUESTÃO 01")
    total_pessoas: int = 0
    total_consumo: float = 0.0
    percentual_servico: float = 0.0
    resultado = 0
    error_message = 'Valor Inválido'
    success_message = 'Dividindo a conta por {0} pessoa(s), cada pessoa deverá pagar R$ {1}'

    print('Insira o total de pessoas: ')
    total_pessoas = int(input())

    if total_pessoas <= 0:
        print(error_message)
        return

    print('Insira o percentual de serviço entre 0 e 100: ')
    percentual_servico = float(input())

    if percentual_servico < 0 or percentual_servico > 100:
        print(error_message)
        return

    print('Insira o total do consumo: R$ ')
    total_consumo = float(input())

    if total_consumo < 0:
        print(error_message)
        return

    resultado = (total_consumo + percentual_servico)/total_pessoas
    resultado = str('%.2f' % resultado).replace('.',',')

    print(success_message.format(total_pessoas, resultado))



def pode_votar():

    print("QUESTÃO 02")
    print('Informe a idade: ')
    idade = int(input())

    if idade > 0:
        if idade < 16:
            print('Não tem direito a voto.')
        elif (16 <= idade < 18) or idade >= 70:
            print('Não tem obrigação de votar')
        elif 18 <= idade < 70:
            print('Tem obrigação de votar.')
    else:
        print('Idade inválida')
        return


def concurso_fantasia():

    print("QUESTÃO 03")
    participantes = []
    notas = []
    maior_nota_index = 0
    nota_anterior = 0

    for i in range(5):

        print('Informe o nome do participante {0}º: '.format(i+1))
        participantes.append(str(input()))
        print('Informe a nota do participante {0}º: '.format(i+1))
        nota = float(input())
        if 0 <= nota <= 10:
            if nota > nota_anterior:
                maior_nota_index = i
                nota_anterior = nota
            notas.append(nota)
        else:
            print('Nota inválida')
            return

    print('O(a) vencedor(a) foi {0} com nota {1}!'.format(participantes[maior_nota_index], notas[maior_nota_index]))


divisao_conta()
pode_votar()
concurso_fantasia()
