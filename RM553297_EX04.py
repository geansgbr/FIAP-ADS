# Função para calcular o fatorial
def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Solicitar ao usuário o número de minutos
minutos = int(input("Digite o número de minutos atuais: "))

# Calcular o fatorial dos minutos
fatorial_minutos = calcular_fatorial(minutos)

# Criar a senha
senha = "LIBERDADE" + str(fatorial_minutos)

# Exibir a senha
print(f"A senha necessária para desbloqueio é: {senha}")
