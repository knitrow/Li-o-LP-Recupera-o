import random


def gerar_senha(tamanho):
   
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%&*()_+-=[]{}|;:,.<>?/~"
    

    todos_caracteres = letras + numeros + simbolos
    
  
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(todos_caracteres) 
    
    return senha


tamanho = int(input("Digite o tamanho da senha desejada: "))


senha_gerada = gerar_senha(tamanho)
print(f"A senha gerada é: {senha_gerada}")

