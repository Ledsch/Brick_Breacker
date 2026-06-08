# =============================================
# FUNÇÕES DE DESENHO NA TELA
# =============================================
import pygame
from constantes import CORES


def desenhar_fundo(tela, jogador, bola):
    """Limpa a tela e desenha o jogador e a bola."""
    tela.fill(CORES["preta"])
    pygame.draw.rect(tela, CORES["azul"],   jogador)
    pygame.draw.rect(tela, CORES["branca"], bola)


def desenhar_blocos(tela, blocos):
    """Desenha todos os blocos ainda presentes na lista."""
    for bloco in blocos:
        pygame.draw.rect(tela, CORES["verde"], bloco)


def desenhar_pontuacao(tela, pontuacao):
    """Renderiza o texto de pontuação no rodapé da tela."""
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontuação: {pontuacao}", True, CORES["amarela"])
    tela.blit(texto, (0, 780))


def desenhar_tela_inicio(tela, recorde):
    """
    Tela inicial com título, subtítulo, comandos e recorde.
    Aguarda o jogador pressionar ENTER ou ESPAÇO.
    """
    largura, altura = tela.get_size()

    fonte_titulo    = pygame.font.Font(None, 90)
    fonte_subtitulo = pygame.font.Font(None, 40)
    fonte_instrucao = pygame.font.Font(None, 30)
    fonte_texto     = pygame.font.Font(None, 28)

    titulo    = fonte_titulo.render("BRICK BREAKER", True, CORES["amarela"])
    subtitulo = fonte_subtitulo.render("Destrua todos os blocos!", True, CORES["branca"])
    instrucao = fonte_instrucao.render("Pressione ENTER ou ESPAÇO para começar", True, CORES["verde"])

    # Controles
    texto_controles_titulo = fonte_texto.render("Controles:", True, CORES["branca"])
    texto_controles1       = fonte_texto.render("← Seta Esquerda: mover para esquerda", True, CORES["branca"])
    texto_controles2       = fonte_texto.render("→ Seta Direita: mover para direita",   True, CORES["branca"])

    # Placar
    texto_placar_titulo = fonte_texto.render("Placar:", True, CORES["amarela"])
    texto_placar        = fonte_texto.render(f"Recorde: {recorde} pontos", True, CORES["amarela"])

    esperando = True
    clock     = pygame.time.Clock()
    contador  = 0
    visivel   = True

    while esperando:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    esperando = False

        tela.fill(CORES["preta"])

        # Título
        pygame.draw.line(tela, CORES["azul"], (50, 190), (largura - 50, 190), 3)
        tela.blit(titulo,    ((largura - titulo.get_width())    // 2, 210))
        tela.blit(subtitulo, ((largura - subtitulo.get_width()) // 2, 300))
        pygame.draw.line(tela, CORES["azul"], (50, 350), (largura - 50, 350), 3)

        # Controles (lado esquerdo)
        tela.blit(texto_controles_titulo, (80, 390))
        tela.blit(texto_controles1,       (80, 425))
        tela.blit(texto_controles2,       (80, 455))

        # Placar (lado direito)
        tela.blit(texto_placar_titulo, (largura - texto_placar_titulo.get_width() - 80, 390))
        tela.blit(texto_placar,        (largura - texto_placar.get_width()        - 80, 425))

        # Linha separadora antes da instrução
        pygame.draw.line(tela, CORES["azul"], (50, 500), (largura - 50, 500), 3)

        # Instrução piscando
        contador += 1
        if contador >= 30:
            visivel  = not visivel
            contador = 0

        if visivel:
            tela.blit(instrucao, ((largura - instrucao.get_width()) // 2, 530))

        pygame.display.flip()


def desenhar_mensagem_fim(tela, vitoria, pontuacao, recorde):
    """
    Tela de fim de jogo com pontuação, recorde e opções.

    Retorna:
        True  → jogar novamente
        False → sair
    """
    largura, altura = tela.get_size()
    clock           = pygame.time.Clock()

    fonte_titulo    = pygame.font.Font(None, 90)
    fonte_pontuacao = pygame.font.Font(None, 40)
    fonte_recorde   = pygame.font.Font(None, 36)
    fonte_opcao     = pygame.font.Font(None, 32)

    if vitoria:
        titulo = fonte_titulo.render("VOCÊ VENCEU!", True, CORES["verde"])
    else:
        titulo = fonte_titulo.render("GAME OVER", True, CORES["branca"])

    texto_pontuacao = fonte_pontuacao.render(
        f"Pontuação final: {pontuacao}", True, CORES["amarela"]
    )
    texto_recorde = fonte_recorde.render(
        f"Recorde: {recorde} pontos", True, CORES["amarela"]
    )

    texto_sim = fonte_opcao.render("ENTER  →  Jogar novamente", True, CORES["verde"])
    texto_nao = fonte_opcao.render("ESC    →  Sair do jogo",    True, CORES["branca"])

    contador = 0
    visivel  = True

    while True:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False

        tela.fill(CORES["preta"])

        pygame.draw.line(tela, CORES["azul"], (50, 180), (largura - 50, 180), 3)
        tela.blit(titulo, ((largura - titulo.get_width()) // 2, 200))

        tela.blit(texto_pontuacao, ((largura - texto_pontuacao.get_width()) // 2, 310))
        tela.blit(texto_recorde,   ((largura - texto_recorde.get_width())   // 2, 360))

        pygame.draw.line(tela, CORES["azul"], (50, 415), (largura - 50, 415), 3)

        contador += 1
        if contador >= 30:
            visivel  = not visivel
            contador = 0

        if visivel:
            tela.blit(texto_sim, ((largura - texto_sim.get_width()) // 2, 460))
            tela.blit(texto_nao, ((largura - texto_nao.get_width()) // 2, 505))

        pygame.display.flip()