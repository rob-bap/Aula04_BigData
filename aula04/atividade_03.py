print('''
[1] - Sul
[2] - Norte
[3] - Leste
[4] - Oeste
[5 e 6] - Nordeste
[7 a 9] - Sudeste
[10] - Centro-Oeste
[11] - Noroeste
''')

regiao = int(input("Em qual região você nasceu?: "))

match regiao:

    case 1:
        print("Sul")
    
    case 2:
        print("Norte")

    case 3:
        print("Leste")

    case 4:
        print("Oeste")
    
    case 5 | 6:
        print("Nordeste")

    case n if 7 <= n <= 9:
        print("Sudeste")
    
    case 10:
        print("Centro-Oeste")
    
    case 11:
        print("Noroeste")

    case _:
        print("Região Inválida")

print("Programa Encerrado")
