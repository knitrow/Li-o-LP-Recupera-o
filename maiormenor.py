
numeros = []


for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)  # Adiciona o número à lista


maior_numero = max(numeros)
menor_numero = min(numeros)


print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
