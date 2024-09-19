def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro do jogo."""
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vencedor(tabuleiro):
    """Verifica se há um vencedor no jogo."""
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != " ":
            return tabuleiro[0][col]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None


def tabuleiro_cheio(tabuleiro):
    """Verifica se o tabuleiro está cheio."""
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


def jogo_da_velha():
    """Função principal para rodar o jogo da velha."""
    # Criar um tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    
    # Indica o jogador atual (X ou O)
    jogador_atual = "X"

    while True:
        # Exibir o tabuleiro
        print(f"Jogador {jogador_atual}'s vez")
        exibir_tabuleiro(tabuleiro)

        # Obter entrada do jogador
        while True:
            try:
                linha = int(input("Digite a linha (1-3): ")) - 1
                coluna = int(input("Digite a coluna (1-3): ")) - 1
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual
                    break
                else:
                    print("Posição já ocupada. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite números entre 1 e 3 para linha e coluna.")
            except IndexError:
                print("Entrada fora do alcance. Digite números entre 1 e 3 para linha e coluna.")

        # Verificar se há um vencedor
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            break

        # Verificar se o tabuleiro está cheio (empate)
        if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        # Alternar jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogo_da_velha()

