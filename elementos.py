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
    IMAGEM_BOLA,
    IMAGEM_JOGADOR,
)


def carregar_imagem_bola():
    """
    Carrega a imagem da bola e redimensiona para o tamanho definido em TAMANHO_BOLA.
    Retorna a imagem pronta para uso.
    """
    try:
        imagem = pygame.image.load(IMAGEM_BOLA).convert_alpha()
        imagem = pygame.transform.scale(imagem, (TAMANHO_BOLA, TAMANHO_BOLA))
        print("Imagem da bola carregada com sucesso!")
    except Exception as e:
        print(f"ERRO ao carregar bola.png: {e}")
        # fallback: cria uma superfície branca se a imagem não for encontrada
        imagem = pygame.Surface((TAMANHO_BOLA, TAMANHO_BOLA))
        imagem.fill((255, 255, 255))
    return imagem


def carregar_imagem_jogador():
    """
    Carrega a imagem do jogador e redimensiona para o tamanho definido em TAMANHO_JOGADOR.
    Retorna a imagem pronta para uso.
    """
    try:
        imagem = pygame.image.load(IMAGEM_JOGADOR).convert_alpha()
        imagem = pygame.transform.scale(imagem, (TAMANHO_JOGADOR, 20))
        print("Imagem do jogador carregada com sucesso!")
    except Exception as e:
        print(f"ERRO ao carregar jogador.png: {e}")
        # fallback: cria uma superfície azul se a imagem não for encontrada
        imagem = pygame.Surface((TAMANHO_JOGADOR, 20))
        imagem.fill((0, 0, 255))
    return imagem


def criar_bola():
    """Cria e retorna o Rect da bola centralizado na tela."""
    bola = pygame.Rect(0, 0, TAMANHO_BOLA, TAMANHO_BOLA)
    bola.center = (TAMANHO_TELA[0] // 2, TAMANHO_TELA[1] // 2)
    return bola


def criar_jogador():
    """Cria e retorna o Rect do jogador na parte inferior da tela."""
    jogador = pygame.Rect(0, 0, TAMANHO_JOGADOR, 20)
    jogador.center = (TAMANHO_TELA[0] // 2, TAMANHO_TELA[1] - 40)
    return jogador


def criar_blocos():
    """Cria e retorna a lista de Rects dos blocos."""
    blocos        = []
    largura_bloco = TAMANHO_TELA[0] // QTDE_BLOCOS_LINHA
    altura_bloco  = 30

    for linha in range(QTDE_LINHAS_BLOCOS):
        for coluna in range(QTDE_BLOCOS_LINHA):
            x = coluna * largura_bloco
            y = 60 + linha * (altura_bloco + 5)
            blocos.append(pygame.Rect(x, y, largura_bloco - 4, altura_bloco))

    return blocos