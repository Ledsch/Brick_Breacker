# =============================================
# CRIAÇÃO DOS ELEMENTOS DO JOGO
# =============================================
import pygame
from constantes import (
    TAMANHO_TELA,
    TAMANHO_BOLA,
    TAMANHO_JOGADOR,
    QTDE_BLOCOS_LINHA,
    QTDE_LINHAS_BLOCOS,
)


def criar_bola():
    """Retorna o Rect inicial da bola."""
    return pygame.Rect(100, 500, TAMANHO_BOLA, TAMANHO_BOLA)


def criar_jogador():
    """Retorna o Rect inicial do jogador."""
    return pygame.Rect(0, 750, TAMANHO_JOGADOR, 15)


def criar_blocos(qtde_por_linha=QTDE_BLOCOS_LINHA, qtde_linhas=QTDE_LINHAS_BLOCOS):
    """
    Gera e retorna uma lista de Rects representando os blocos.
    Por padrão usa as constantes definidas em constantes.py.
    """
    largura_tela = TAMANHO_TELA[0]
    distancia_entre = 5
    largura_bloco = largura_tela / qtde_por_linha - distancia_entre
    altura_bloco = 15
    espacamento_vertical = altura_bloco + 10

    blocos = []
    for linha in range(qtde_linhas):
        for coluna in range(qtde_por_linha):
            bloco = pygame.Rect(
                coluna * (largura_bloco + distancia_entre),
                linha * espacamento_vertical,
                largura_bloco,
                altura_bloco,
            )
            blocos.append(bloco)
    return blocos
