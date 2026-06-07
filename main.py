# =============================================
# PONTO DE ENTRADA DO JOGO
# =============================================
import pygame
import sys

from constantes import FPS, VELOCIDADE_BOLA, MUSICA_FUNDO
from elementos  import criar_bola, criar_jogador, criar_blocos
from desenho    import (
    desenhar_fundo,
    desenhar_blocos,
    desenhar_pontuacao,
    desenhar_mensagem_fim,
    desenhar_tela_inicio,
)
from logica import movimentar_jogador, movimentar_bola, verificar_vitoria


def inicializar():
    pygame.init()
    tela  = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brick Breaker")
    return tela, clock


def iniciar_musica():
    """Carrega e toca a música de fundo em loop infinito."""
    pygame.mixer.music.load(MUSICA_FUNDO)  # carrega o arquivo
    pygame.mixer.music.set_volume(0.5)     # volume de 0.0 a 1.0
    pygame.mixer.music.play(-1)            # -1 = loop infinito


def parar_musica():
    """Para a música completamente."""
    pygame.mixer.music.stop()


def main():
    tela, clock = inicializar()

    # ← Inicia a música antes da tela de início
    iniciar_musica()

    desenhar_tela_inicio(tela)

    while True:
        bola      = criar_bola()
        jogador   = criar_jogador()
        blocos    = criar_blocos()
        movimento = VELOCIDADE_BOLA[:]
        rodando   = True
        vitoria   = False

        while rodando:
            clock.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    parar_musica()
                    pygame.quit()
                    sys.exit()

            movimentar_jogador(jogador)
            movimento = movimentar_bola(bola, jogador, blocos, movimento)

            if movimento is None:
                rodando = False
                vitoria = False
            elif verificar_vitoria(blocos):
                rodando = False
                vitoria = True

            desenhar_fundo(tela, jogador, bola)
            desenhar_blocos(tela, blocos)
            desenhar_pontuacao(tela, len(criar_blocos()) - len(blocos))
            pygame.display.flip()

        pontuacao     = len(criar_blocos()) - len(blocos)
        jogar_de_novo = desenhar_mensagem_fim(tela, vitoria, pontuacao)

        if not jogar_de_novo:
            parar_musica()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()