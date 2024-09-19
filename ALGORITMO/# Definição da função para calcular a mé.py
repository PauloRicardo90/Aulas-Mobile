# Definição da função para calcular a média e determinar o status do aluno
def calcular_status(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Lista para armazenar as notas do aluno
notas_aluno = [ ]

# Ler as notas do aluno
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas_aluno.append(nota)

# Chamar a função para calcular a média e determinar o status do aluno
status_aluno = calcular_status(notas_aluno)

# Exibir o status do aluno
print("Status do aluno:", status_aluno)