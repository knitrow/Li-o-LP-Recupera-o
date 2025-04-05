import random


numero_secreto = random.randint(1, 10)


tentativas = 0


print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")


while True:
    
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1  

    
    if palpite < numero_secreto:
        print("O número é maior. Tente novamente!")
    elif palpite > numero_secreto:
        print("O número é menor. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break  