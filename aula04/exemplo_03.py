# estrutura de print usada para apresenta o texto da maneira exata que está escrita
print('''
[1] - Marketing
[2] - Financeiro
[3 a 5] - ADM
[6 a 9] - T.I.
[10 a 20] - Serviços Gerais 
''')

codigo = int(input("Escolha uma opção: "))

match codigo:  # estrutura usada para várias condições de uma variavel

    case 1:
        print("Marketing")
        
    case 2:
        print("Financeiro")

    case 3 | 4 | 5:  # pipe = desreve condições exatas em um caso
        print("ADM")

    case numero if 6 <= numero <= 9:  # "apelido" usado para definir a variavel dentro do case, podendo ter o mesmo nome da varivel definida ao inicio
        print("T.I.")

    case numero if 10 <= numero <= 20:
        print("Serviços Gerais")

    case _:
        print("Código Inválido")

print("Programa Finalizado")