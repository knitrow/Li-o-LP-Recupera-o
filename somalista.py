# Função que calcula a soma dos elementos de uma lista
def somar_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero  # Adiciona cada número da lista à variável soma
    return soma

# Exemplo de lista de números
numeros = [1, 2, 3, 4, 5]

# Chama a função e exibe o resultado
resultado = somar_lista(numeros)
print(f"A soma dos elementos da lista é: {resultado}")
