media = 0

for x in range(4):
    nota = float(input("Digite uma nota: "))
    media += nota

print("Aprovado" if (media/4 >=7) else "Reprovado")
