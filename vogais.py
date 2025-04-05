
frase = input("Digite uma frase: ")


contador_vogais = 0
vogais = "aeiouAEIOU"
for letra in frase:
    if letra in vogais:  # Verifica se o caractere é uma vogal
        contador_vogais += 1


print(f"A frase contém {contador_vogais} vogais.")
