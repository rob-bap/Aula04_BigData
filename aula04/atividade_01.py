salario = float(input("Digite seu salário: "))
vendas = float(input("Qual foi seu valor total de vendas?: "))
bonus = 100
esforco = salario + 20

if vendas > 1000:
    salario_bonus = salario + bonus
    print(f"Parabéns! Você vendeu obteve R${vendas} em vendas, seu salário de R${salario} recebera um aumento de R${bonus}, totalizando R${salario_bonus}.")
else:
    print(f"Você obteve R${vendas} em vendas, pelo seu esforço na colaboração, seu salário de R${salario} recebera um aumento de R$20, totalizando R${esforco}")