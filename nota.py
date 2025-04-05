
nota = float(input("Digite a nota do aluno (0 a 10): "))


if 0 <= nota <= 10:
    
    if nota >= 6:
        print("Aluno foi muito bem, aprovado!")
    else:
        print("Aluno foi mal, reprovado!")
else:
    print("Nota inválida! A nota deve estar entre 0 e 10.")

