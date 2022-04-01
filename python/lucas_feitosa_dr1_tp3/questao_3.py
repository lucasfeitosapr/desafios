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

concurso_fantasia()
