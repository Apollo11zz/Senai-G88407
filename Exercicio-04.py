def calcularCustoViagem(distancia, tipoVeiculo):
    if tipoVeiculo == "CARRO":
        custoPorKm = 0.5
    elif tipoVeiculo == "MOTO":
        custoPorKm = 0.2
    elif tipoVeiculo == "BICICLETA":
        custoPorKm = 0.1
    else:
        return None
    
    custoTotal = distancia * custoPorKm
    return custoTotal

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

custo = calcularCustoViagem(distanciaDaViagem, veiculo)
if custo == None:
    print("Tipo de veículo inválido!")
else:
    print("O custo total da viagem é: R${:.2f}".format(custo))
