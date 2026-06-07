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


def desenhar_tela_inicio(tela):
    """
    Desenha a tela de início do jogo com título e instrução.
    Fica em loop até o jogador pressionar ENTER ou ESPAÇO.
    """
    largura, altura = tela.get_size()

    fonte_titulo    = pygame.font.Font(None, 90)
    fonte_subtitulo = pygame.font.Font(None, 40)
    fonte_instrucao = pygame.font.Font(None, 30)

    titulo    = fonte_titulo.render("BRICK BREAKER", True, CORES["amarela"])
    subtitulo = fonte_subtitulo.render("Destrua todos os blocos!", True, CORES["branca"])
    instrucao = fonte_instrucao.render("Pressione ENTER ou ESPAÇO para começar", True, CORES["verde"])

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
        pygame.draw.line(tela, CORES["azul"], (50, 200), (largura - 50, 200), 3)
        tela.blit(titulo,    ((largura - titulo.get_width())    // 2, 220))
        tela.blit(subtitulo, ((largura - subtitulo.get_width()) // 2, 330))
        pygame.draw.line(tela, CORES["azul"], (50, 390), (largura - 50, 390), 3)

        contador += 1
        if contador >= 30:
            visivel  = not visivel
            contador = 0

        if visivel:
            tela.blit(instrucao, ((largura - instrucao.get_width()) // 2, 500))

        pygame.display.flip()


def desenhar_mensagem_fim(tela, vitoria, pontuacao):
    """
    Exibe a tela de fim de jogo.

    Retorna:
        True  → jogador quer jogar novamente
        False → jogador quer sair
    """
    largura, altura = tela.get_size()
    clock           = pygame.time.Clock()

    fonte_titulo    = pygame.font.Font(None, 90)
    fonte_pontuacao = pygame.font.Font(None, 40)
    fonte_opcao     = pygame.font.Font(None, 36)

    # Textos principais
    if vitoria:
        titulo = fonte_titulo.render("VOCÊ VENCEU!", True, CORES["verde"])
    else:
        titulo = fonte_titulo.render("GAME OVER", True, CORES["branca"])

    texto_pontuacao = fonte_pontuacao.render(
        f"Pontuação final: {pontuacao}", True, CORES["amarela"]
    )

    # Opções
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
                    return True   # ← jogar novamente
                if evento.key == pygame.K_ESCAPE:
                    return False  # ← sair

        # Fundo
        tela.fill(CORES["preta"])

        # Linha decorativa
        pygame.draw.line(tela, CORES["azul"], (50, 180), (largura - 50, 180), 3)

        # Título (Game Over ou Você Venceu)
        tela.blit(titulo, ((largura - titulo.get_width()) // 2, 200))

        # Pontuação
        tela.blit(texto_pontuacao, ((largura - texto_pontuacao.get_width()) // 2, 320))

        # Linha decorativa
        pygame.draw.line(tela, CORES["azul"], (50, 390), (largura - 50, 390), 3)

        # Opções piscando
        contador += 1
        if contador >= 30:
            visivel  = not visivel
            contador = 0

        if visivel:
            tela.blit(texto_sim, ((largura - texto_sim.get_width()) // 2, 450))
            tela.blit(texto_nao, ((largura - texto_nao.get_width()) // 2, 510))

        pygame.display.flip()