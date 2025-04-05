
numeros = [33, 45, 72, 2, 5, 88,88,88,99,99,135,34,55,33,98,33,53,22,33, 5, 9, 2]


numero_procurado = int(input("Digite um número para contar quantas vezes ele aparece na lista: "))


contador = numeros.count(numero_procurado)


print(f"O número {numero_procurado} aparece {contador} vez(es) na lista.")
