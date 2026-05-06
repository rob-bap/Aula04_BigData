# tempo_casa = float(input("Quanto anos de casa você possui?: "))
# if tempo_casa >= 5:
#     print(f'Parabéns! Você está qualificado para receber um bônus, pois possui {tempo_casa} anos de casa.')
    
# else:
#     print(f'Você não está qualificado para receber bônus, pois ainda faltam {5 - tempo_casa} ano(s) de casa.')

# ------------------------------------------------------
    
# verificar o consume de um carro
# se o concumo for maior que 12km/l - economico
# menor que 12km/l - nãp economico
    
distancia = float(input("Informe a distância percorrida em km: "))
combustivel = float(input("Informe o combustível gasto em litros: "))

consumo = distancia / combustivel

if consumo >= 12:
    print(f"Parabéns! Seu veículo é econômico, pois obteve um consumo de {consumo} km/l.")

else:
    print(f'Seu veículo não é econômico, pois obteve um consumo de {consumo} km/l, prepare seu bolso')