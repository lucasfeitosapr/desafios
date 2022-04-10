
percentages = {'m': 30,
               'e': 20,
               't': 15}


def calc_renda():

    common_result = "Seus gastos totais com {} comprometem {}% da sua renda total. O máximo recomendado é de {}%"
    under_result = " Seus gastos estão dentro da margem recomendada"
    above_result = " Portanto, idealmente, o máximo de sua renda comprometida com {} deveria ser de R$ {}"

    salario = float(input("Renda mensal total: R$ "))

    expenses = {'moradia': float(input("Gastos totais com moradia: R$ ")),
                'educação': float(input("Gastos totais com educação: R$ ")),
                'transporte': float(input("Gastos totais com transporte: R$ "))}
 
    expenses_percentage = get_expenses_percentage(salario, expenses)
    print("----------------------------------------------------------------------")

    for key, value in expenses_percentage.items():
        if is_under_recommended_percentage(value, key[0]):

            print(common_result.format(key, value, percentages[key[0]]) + under_result)

        else:

            print(common_result.format(key, value, percentages[key[0]]) +
                  above_result.format(key, get_expected_percentage(key, salario)))


def get_expected_percentage(which_expense, expense_value):
    return (percentages[which_expense[0]] * expense_value) / 100


def get_expenses_percentage(salario, expenses):
    expenses_percentage = {}
    for key, value in expenses.items():
        expenses_percentage[key] = value_to_percentage(salario, value)
    return expenses_percentage


def is_under_recommended_percentage(percent, which_percentage):
    return percent <= percentages[which_percentage]


def value_to_percentage(salario, amount):
    return (amount*100)/salario


calc_renda()
