quantidade = int(input("Digite a quantidade de números: "))
numeros = []
soma = 0

for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
    soma += numero
    media = soma / quantidade

print(f"\nMédia: {media:.2f}")

amplitude = max(numeros) - min(numeros)
print(f"\nAmplitude: {amplitude}")

variancia = sum((x - media) ** 2 for x in numeros) / quantidade
print(f"\nVariância: {variancia:.2f}")