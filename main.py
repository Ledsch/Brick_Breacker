# =============================================
# PONTO DE ENTRADA DO JOGO
# DESENVOVEDOR: LEONARDO M S.
# FACULDADE: UNINTER
# =============================================
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
    """Inicializa o pygame e retorna a tela e o clock."""
    pygame.init()
    pygame.mixer.init()  # ← inicializa o mixer de áudio separadamente
    tela  = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brick Breaker")
    return tela, clock


def iniciar_musica():
    """Carrega e toca a música de fundo em loop infinito."""
    print("Tentando carregar música em:", MUSICA_FUNDO)
    try:
        pygame.mixer.music.load(MUSICA_FUNDO)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 = loop infinito
        print("Música carregada e tocando!")
    except Exception as e:
        print("ERRO ao carregar música:", e)


def parar_musica():
    """Para a música completamente."""
    pygame.mixer.music.stop()


def main():
    tela, clock = inicializar()

    # Inicia a música antes de qualquer tela
    iniciar_musica()

    recorde = 0
    desenhar_tela_inicio(tela, recorde)

    # Loop externo: controla se vai reiniciar ou sair
    while True:

        # Reinicia todos os elementos a cada nova partida
        bola      = criar_bola()
        jogador   = criar_jogador()
        blocos    = criar_blocos()
        movimento = VELOCIDADE_BOLA[:]
        rodando   = True
        vitoria   = False
        pontuacao = 0

        # Loop interno: loop principal do jogo
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

            # Pontuação = blocos destruídos
            pontuacao = len(criar_blocos()) - len(blocos)

            desenhar_fundo(tela, jogador, bola)
            desenhar_blocos(tela, blocos)
            desenhar_pontuacao(tela, pontuacao)
            pygame.display.flip()

        # Atualiza recorde se a pontuação atual for maior
        if pontuacao > recorde:
            recorde = pontuacao

        # Tela de fim de jogo
        jogar_de_novo = desenhar_mensagem_fim(tela, vitoria, pontuacao, recorde)

        if not jogar_de_novo:
            parar_musica()
            pygame.quit()
            sys.exit()

        # Mostra a tela inicial novamente com o recorde atualizado
        desenhar_tela_inicio(tela, recorde)


if __name__ == "__main__":
    main()