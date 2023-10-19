# Defina uma lista para armazenar os nomes dos dias da semana.
dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

# Crie uma lista para armazenar a contagem de votos para cada dia.
votos_dias = []

# Solicite ao usuário a quantidade de votos para cada dia da semana.
for dia in dias_semana:
    votos = int(input(f"Digite a quantidade de votos para {dia}: "))
    votos_dias.append(votos)

# Encontre o dia com o maior número de votos.
dia_escolhido = dias_semana[votos_dias.index(max(votos_dias))]

# Exiba o dia escolhido.
print(f"O dia escolhido com mais votos foi: {dia_escolhido}")
