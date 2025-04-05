valor = int(input("Digite o valor que você deseja sacar: R$ "))


notas_100 = valor // 100
valor %= 100  


notas_50 = valor // 50
valor %= 50  


notas_20 = valor // 20
valor %= 20 


notas_10 = valor // 10
valor %= 10  


notas_1 = valor // 1
valor %= 1  

print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Moedas de 1: {notas_1}")