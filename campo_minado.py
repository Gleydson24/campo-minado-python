import random


def inicializar_campo(linhas, colunas, minas):
    campo_invisivel = [["0" for _ in range(colunas)] for _ in range(linhas)]
    campo_visivel = [["-" for _ in range(colunas)] for _ in range(linhas)]

    minas_colocadas = 0
    while minas_colocadas < minas:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if campo_invisivel[linha][coluna] != "X":
            campo_invisivel[linha][coluna] = "X"
            minas_colocadas += 1

    return campo_invisivel, campo_visivel


def contar_minas(campo, l, c, linhas, colunas):
        total = 0
        for i in range(l - 1, l + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i < linhas and 0 <= j < colunas and campo[i][j] == "X":
                    total += 1
        return total


def mostrar_campo(campo):
    print("\nCampo:")
    for linha in campo:
        print(" ".join(linha))


def main():
    linhas = 5
    colunas = 5
    minas = 3

    campo_invisivel, campo_visivel = inicializar_campo(linhas, colunas, minas)

    for l in range(linhas):
        for j in range(colunas):
            if campo_invisivel[l][j] != "X":
                campo_invisivel[l][j] = str(
                    contar_minas(campo_invisivel, l, j, linhas, colunas))

    jogadas = 0
    while True:
        mostrar_campo(campo_visivel)

        try:
            linha = int(input(f"Digite a linha (0 a {linhas-1}): "))
            coluna = int(input(f"Digite a coluna (0 a {colunas-1}): "))

            if not (0 <= linha < linhas and 0 <= coluna < colunas):
                print("Posição inválida! Tente novamente.")
                continue

        except ValueError:
            print("Por favor, digite números válidos!")
            continue

        if campo_invisivel[linha][coluna] == "X":
            print("\nVocê Perdeu! Aqui tinha uma mina!")
            mostrar_campo(campo_invisivel)
            break
        else:
            campo_visivel[linha][coluna] = campo_invisivel[linha][coluna]
            jogadas += 1

        if jogadas == (linhas * colunas - minas):
            print("\nParabéns! Você ganhou!")
            mostrar_campo(campo_invisivel)
            break


if __name__ == "__main__":
    main()
