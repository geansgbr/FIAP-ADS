# Inicialize listas para armazenar as notas dos alunos pares e ímpares.
notas_pares = []
notas_impares = []

# Loop para inserir as notas dos alunos pares.
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
for i in range(2, 51, 2):  # Números pares de 2 a 50
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    notas_pares.append(nota)

# Loop para inserir as notas dos alunos ímpares.
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
for i in range(1, 50, 2):  # Números ímpares de 1 a 49
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    notas_impares.append(nota)

# Calcule a média das notas para cada metade da sala.
media_pares = sum(notas_pares) / len(notas_pares)
media_impares = sum(notas_impares) / len(notas_impares)

# Determine qual metade teve a maior nota.
if media_pares > media_impares:
    maior_metade = "pares"
elif media_impares > media_pares:
    maior_metade = "ímpares"
else:
    maior_metade = "ambas as metades (empate)"

# Exiba as médias e qual metade teve a maior nota.
print(f"A média das notas dos alunos pares é: {media_pares:.2f}")
print(f"A média das notas dos alunos ímpares é: {media_impares:.2f}")
print(f"A metade com a maior nota é: {maior_metade}")
