# =============================================
# PONTO DE ENTRADA DO JOGO
# DESENVOVEDOR: LEONARDO M S.
# FACULDADE: UNINTER
# =============================================
import pygame
import sys
import os

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
    pygame.mixer.init()  # ← inicializa o áudio separadamente
    tela  = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brick Breaker")
    return tela, clock


def iniciar_musica():
    """Carrega e toca a música em loop infinito."""
    try:
        pygame.mixer.music.load(MUSICA_FUNDO)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Música carregada com sucesso!")  # ← aparece no console
    except pygame.error as e:
        print(f"Erro ao carregar música: {e}")  # ← mostra o erro real


def parar_musica():
    pygame.mixer.music.stop()


def main():
    tela, clock = inicializar()

    iniciar_musica()  # ← toca antes de qualquer tela

    recorde = 0
    desenhar_tela_inicio(tela, recorde)

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

            total_blocos = len(criar_blocos())
            pontuacao    = total_blocos - len(blocos)

            desenhar_fundo(tela, jogador, bola)
            desenhar_blocos(tela, blocos)
            desenhar_pontuacao(tela, pontuacao)
            pygame.display.flip()

        if pontuacao > recorde:
            recorde = pontuacao

        jogar_de_novo = desenhar_mensagem_fim(tela, vitoria, pontuacao, recorde)

        if not jogar_de_novo:
            parar_musica()
            pygame.quit()
            sys.exit()

        desenhar_tela_inicio(tela, recorde)


if __name__ == "__main__":
    main()