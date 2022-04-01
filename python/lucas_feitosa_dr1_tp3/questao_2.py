

def pode_votar():
    print("QUESTÃO 02")
    print('Informe a idade: ')
    idade = int(input())

    print(valida_idade(idade))


def valida_idade(idade):
    if idade > 0:
        if idade < 16:
            return 'Não tem direito a voto.'
        elif (16 <= idade < 18) or idade >= 70:
            return 'Não tem obrigação de votar'
        elif 18 <= idade < 70:
            return 'Tem obrigação de votar.'
    else:
        return 'Idade inválida'


pode_votar()
