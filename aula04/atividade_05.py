valor = float(input("Digite o valor da venda: "))

match valor:

    case n if n < 100:
        print("Sua venda se caracteriza como pequena.")

    case n if 100 <= n < 500:
        print("Sua venda se caracteriza como média.")

    case n if n >= 500:
        print("Sua venda se caracteriza como grande.")