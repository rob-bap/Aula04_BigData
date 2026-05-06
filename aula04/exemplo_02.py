# Teste para duas situaçõs
# setor = A e tempo de casa minimo 3 anos, aumento de 18%
# caso contrario, aumento de 9%

tempo = float(input("Informe seu tempo de casa: "))
setor = input("Informe o seu setor: ").upper()  # definir entrada para maiusculo
salario = float(input("Informe seu selário: "))

if setor == "A" and tempo >= 3:  # "and" define todas as condições como verdadeira para entrar no if e "or" para qualquer uma das condições serem aceitas
    print("\n18%")  # "\n" dentro do texto para pular uma linha
    aumento = salario * 0.18
    novo_salario = salario + aumento
else:
    print("\n9%")
    aumento = salario * 0.09
    novo_salario = salario + aumento

print(f"\nAumento de {aumento:.2f}")
print(f"\nNovo salário de {novo_salario:.2f}")
