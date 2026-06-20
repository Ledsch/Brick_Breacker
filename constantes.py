# =============================================
# CONSTANTES GLOBAIS DO JOGO
# =============================================
import os
import sys

# Detecta se está rodando como .exe ou como script normal no PyCharm
if getattr(sys, "frozen", False):
    PASTA_BASE = sys._MEIPASS
else:
    PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

TAMANHO_TELA       = (800, 800)
TAMANHO_BOLA       = 15
TAMANHO_JOGADOR    = 100
QTDE_BLOCOS_LINHA  = 8
QTDE_LINHAS_BLOCOS = 5
QTDE_TOTAL_BLOCOS  = QTDE_BLOCOS_LINHA * QTDE_LINHAS_BLOCOS
FPS                = 60

VELOCIDADE_BOLA    = [7, -7]
VELOCIDADE_JOGADOR = 10

# Caminhos de áudio e imagens
MUSICA_FUNDO   = os.path.join(PASTA_BASE, "assets", "ratta.mp3")
IMAGEM_BOLA    = os.path.join(PASTA_BASE, "assets", "bola.png")     # ← novo
IMAGEM_JOGADOR = os.path.join(PASTA_BASE, "assets", "jogador.png")  # ← novo

CORES = {
    "branca":  (255, 255, 255),
    "preta":   (0,   0,   0),
    "amarela": (255, 255, 0),
    "azul":    (0,   0,   255),
    "verde":   (0,   255, 0),
}