import random

def escolher_palavra():
    """Escolhe uma palavra aleatória de uma lista de palavras."""
    palavras = ["python", "programação", "computador", "tecnologia", "inteligência", "algoritmo"]
    return random.choice(palavras)


def exibir_forca(tentativas_restantes):
    """Exibe o estado atual da forca com base no número de tentativas restantes."""
    estagios = [
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  /
         |
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |
         |
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |
         |
        """,
        """
         -----
         |   |
         |   O
         |   |
         |
         |
        """,
        """
         -----
         |   |
         |   O
         |
         |
         |
        """,
        """
         -----
         |   |
         |
         |
         |
         |
        """
    ]
    print(estagios[tentativas_restantes])


def jogo_da_forca():
    """Função principal para rodar o jogo da forca."""
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = ["_"] * len(palavra_secreta)
    tentativas_restantes = 6
    letras_usadas = set()

    print("Bem-vindo ao jogo da forca!")

    while tentativas_restantes > 0:
        print("\nPalavra: ", " ".join(letras_adivinhadas))
        print(f"Letras usadas: {', '.join(sorted(letras_usadas))}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        # Obter entrada do jogador
        letra = input("Digite uma letra: ").lower()

        # Verificar se a letra já foi usada
        if letra in letras_usadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Adicionar a letra à lista de letras usadas
        letras_usadas.add(letra)

        # Verificar se a letra está na palavra secreta
        if letra in palavra_secreta:
            # Atualizar as letras adivinhadas
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_adivinhadas[i] = letra
            print("Correto! A letra está na palavra.")
        else:
            tentativas_restantes -= 1
            print("Errado! A letra não está na palavra.")
            exibir_forca(tentativas_restantes)

        # Verificar se o jogador venceu
        if "_" not in letras_adivinhadas:
            print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
            return

    # Se as tentativas acabarem, o jogador perde
    print("\nVocê perdeu! A palavra era:", palavra_secreta)


if __name__ == "__main__":
    jogo_da_forca()
