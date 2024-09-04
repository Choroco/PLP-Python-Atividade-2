i = 0
valorTotal = 0

qNotas = int(input("Quantas notas serão necessárias para calcular a média? "))

while(i < qNotas):
    i += 1
    notaAtual = float(input("{}. Nota: ".format(i)))
    valorTotal += notaAtual

print("Aprovado" if (valorTotal/qNotas >=7) else "Reprovado")