# Defina um dicionário para armazenar os tipos de assinatura e as porcentagens de bônus correspondentes.
tabela_porcentagens = {
    "basic": 0.30,
    "silver": 0.20,
    "ouro": 0.10,
    "platinum": 0.5
}

# Solicite ao usuário o tipo de assinatura e o faturamento anual.
tipo_assinatura = input("Digite o tipo de assinatura do cliente (basic/silver/ouro/platinum): ").lower()
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

# Verifique se o tipo de assinatura inserido é válido.
if tipo_assinatura in tabela_porcentagens:
    # Recupere a porcentagem de bônus com base no tipo de assinatura.
    porcentagem_bonus = tabela_porcentagens[tipo_assinatura]

    # Calcule o valor do bônus.
    valor_bonus = faturamento_anual * porcentagem_bonus

    # Exiba o valor do bônus.
    print(f"O valor do bônus que o cliente deve pagar é de R${valor_bonus:.2f}")
else:
    print("Tipo de assinatura inválido. Por favor, insira um tipo de assinatura válido.")






