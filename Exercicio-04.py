# Por: VICTOR GABRIEL DE JESUS MOURA
# SENAI CAMAÇARI - CURSO TECNICO DE DESENVOLVIMENTO DE SISTEMAS
# DEZEMBRO DE 2023

import funcoes

distanciaDaViagem = float(input("Digite a distancia da viagem(Km): "))
veiculo = int(input("\tInforme o Tipo de veículo\n(1)CARRO\t(2)MOTO\t\t(3)BICICLETA\n"))
if veiculo == 1:
    veiculo = "CARRO"
elif veiculo == 2:
    veiculo = "MOTO"
elif veiculo == 3:
    veiculo = "BICICLETA"
else:
    veiculo = "INVALIDO"

custo = funcoes.calcularCustoViagem(distanciaDaViagem, veiculo)
if custo == None:
    print("Tipo de veículo inválido!")
else:
    print("O custo total da viagem é: R${:.2f}".format(custo))
