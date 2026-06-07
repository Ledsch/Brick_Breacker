# =============================================
# FUNÇÕES DE LÓGICA E MOVIMENTAÇÃO
# =============================================
import pygame
from constantes import TAMANHO_TELA, VELOCIDADE_JOGADOR


def movimentar_jogador(jogador):
    """
    Move o jogador verificando se a tecla está SENDO SEGURADA.
    Isso garante movimento contínuo e suave.
    """
    teclas = pygame.key.get_pressed()  # captura o estado atual de todas as teclas

    if teclas[pygame.K_RIGHT]:
        if jogador.right < TAMANHO_TELA[0]:
            jogador.x += VELOCIDADE_JOGADOR

    if teclas[pygame.K_LEFT]:
        if jogador.left > 0:
            jogador.x -= VELOCIDADE_JOGADOR


def movimentar_bola(bola, jogador, blocos, movimento):
    """
    Atualiza a posição da bola e verifica todas as colisões.

    Retorna:
        list  → movimento atualizado (jogo continua)
        None  → bola caiu (fim de jogo)
    """
    bola.x += movimento[0]
    bola.y += movimento[1]

    # Colisão com paredes laterais
    if bola.left <= 0 or bola.right >= TAMANHO_TELA[0]:
        movimento[0] *= -1

    # Colisão com o teto
    if bola.top <= 0:
        movimento[1] *= -1

    # Bola saiu pela base → fim de jogo
    if bola.bottom >= TAMANHO_TELA[1]:
        return None

    # Colisão com o jogador
    if jogador.colliderect(bola):
        movimento[1] *= -1

    # Colisão com blocos
    for bloco in blocos[:]:
        if bloco.colliderect(bola):
            blocos.remove(bloco)
            movimento[1] *= -1
            break

    return movimento


def verificar_vitoria(blocos):
    """Retorna True se todos os blocos foram destruídos."""
    return len(blocos) == 0
