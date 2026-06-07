import os

# =============================================
# CONSTANTES GLOBAIS DO JOGO
# =============================================

TAMANHO_TELA       = (800, 800)
TAMANHO_BOLA       = 15
TAMANHO_JOGADOR    = 100
QTDE_BLOCOS_LINHA  = 8
QTDE_LINHAS_BLOCOS = 5
QTDE_TOTAL_BLOCOS  = QTDE_BLOCOS_LINHA * QTDE_LINHAS_BLOCOS
FPS                = 60

VELOCIDADE_BOLA    = [7, -7]
VELOCIDADE_JOGADOR = 10

MUSICA_FUNDO = os.path.join("assets", "ratta.mp3")

CORES = {
    "branca":  (255, 255, 255),
    "preta":   (0,   0,   0),
    "amarela": (255, 255, 0),
    "azul":    (0,   0,   255),
    "verde":   (0,   255, 0),
}