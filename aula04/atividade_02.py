# Verificar condição de compra para desconto

valor = float(input("Digite o valor da compra feita pelo cliente: "))
forma = input("Digite a forma de pagamento: ").upper().strip()

if forma == "PIX" and valor > 250:
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f'\nTotal da compra do cliente com desconto é de {valor_final}')

else:
    print(f'\nTotal da compra do cliente {valor}')