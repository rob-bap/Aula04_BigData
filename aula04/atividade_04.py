numero = float(input("Digite um número inteiro ou decimal: "))

match numero:
    case n if n > 0:
        print("Seu número digitado é positivo.")

    case n if n < 0:
        print("Seu número digitado é negativo.")

    case n if n == 0:
        print("Seu número digititado é igual a zero")