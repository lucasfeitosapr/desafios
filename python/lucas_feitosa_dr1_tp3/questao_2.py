
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


pode_votar()
