pessoas = {}


quantidade = int(input("Quantas pessoas você deseja cadastrar? "))


for i in range(quantidade):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    
 
    pessoas[nome] = idade


print("\nPessoas maiores de idade (18 anos ou mais):")
for nome, idade in pessoas.items():
    if idade >= 18:
        print(f"{nome} - {idade} anos")