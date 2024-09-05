import random

def jogo_pontuacao():
    #Escolhe um número aleatório entre 1 e 100
    numero_correto = random.randint(1, 100)

    tentativas = 0
    pontuacao = 100
    limite_tentativas = 10

    # Loop principal
    while tentativas < limite_tentativas:
        palpite = input(f"Adivinhe o número (entre 1 e 100). Pontuação: {pontuacao}: ")

        # Verifica se o valor digitado é válido (números fora do intervalo ou entradas não numéricas)
        if not palpite.isdigit() or int(palpite) < 1 or int(palpite) > 100:
            print("Entrada inválida. Por favor, digite um número entre 1 e 100.")
            continue

        # Converte o palpite para inteiro
        palpite = int(palpite)

        tentativas += 1

        # Verificação do palpite
        if palpite == numero_correto:
            print("Correto!")
            print(f"Você acertou o número em {tentativas} tentativas com {pontuacao} pontos.")
            break
        elif palpite < numero_correto:
            print("Muito baixo!")
            pontuacao -= 10
        else:
            print("Muito alto!")
            pontuacao -= 10

    # Verifica se atingiu o limite de tentativas
    else:
        print(f"Você atingiu o limite de tentativas. O número correto era {numero_correto}.")

#Função do jogo em formato multiplayer. Aqui não há limite de tentativas. O jogador que acertar o número primeiro vence. 
def jogo_multiplayer():
    numero_correto = random.randint(1, 100)
    tentativas_jogador1 = 0
    tentativas_jogador2 = 0

    # Loop principal
    while True:
        # Jogador 1
        palpite_jogador1 = input("Jogador 1, adivinhe o número (entre 1 e 100): ")

        # Verifica se o valor digitado é válido (números fora do intervalo ou entradas não numéricas)
        if not palpite_jogador1.isdigit() or int(palpite_jogador1) < 1 or int(palpite_jogador1) > 100:
            print("Entrada inválida. Por favor, digite um número entre 1 e 100.")
            continue

        # Converte o palpite para inteiro
        palpite_jogador1 = int(palpite_jogador1)

        tentativas_jogador1 += 1

        # Verifica se o palpite está correto
        if palpite_jogador1 == numero_correto:
            print(f"Jogador 1 acertou o número em {tentativas_jogador1} tentativas!")
            break

        # Jogador 2
        palpite_jogador2 = input("Jogador 2, adivinhe o número (entre 1 e 100): ")

        # Verifica a entrada do jogador 2
        if not palpite_jogador2.isdigit() or int(palpite_jogador2) < 1 or int(palpite_jogador2) > 100:
            print("Entrada inválida. Por favor, digite um número entre 1 e 100.")
            continue

        # Converte o palpite para inteiro
        palpite_jogador2 = int(palpite_jogador2)

        tentativas_jogador2 += 1

        # Verifica se o palpite está correto
        if palpite_jogador2 == numero_correto:
            print(f"Jogador 2 acertou o número em {tentativas_jogador2} tentativas!")
            break

        # Feedback do jogo para os jogadores
        if palpite_jogador1 < numero_correto:
            print("Jogador 1: Muito baixo!")
        elif palpite_jogador1 > numero_correto:
            print("Jogador 1: Muito alto!")

        if palpite_jogador2 < numero_correto:
            print("Jogador 2: Muito baixo!")
        elif palpite_jogador2 > numero_correto:
            print("Jogador 2: Muito alto!")

# Escolha do modo de jogo
print("Bem-vindo ao Jogo de Adivinhação de Números!")
print("1. Modo Pontuação")
print("2. Modo Multiplayer")
modo = input("Escolha o modo de jogo (1 ou 2): ")

if modo == "1":
    jogo_pontuacao()
elif modo == "2":
    jogo_multiplayer()
else:
    print("Opção inválida. Saindo do jogo.")