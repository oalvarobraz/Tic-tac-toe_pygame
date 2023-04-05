import pygame
from gameBoard import GameBoard, Stats

import tkinter as tk
from tkinter import messagebox

SCREEN_SIZE = (1280, 720)


def show_board(board, screen):
    square_positions = [(i * SQUARE_SIZE + grid_x, j * SQUARE_SIZE + grid_y) for i in range(NUM_SQUARES) for j in range(
        NUM_SQUARES)]

    for i, position in enumerate(square_positions):
        pygame.draw.rect(screen, WHITE, (position[0], position[1], SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)

    # Desenhando as jogadas no tabuleiro
    for i, row in enumerate(board.board):
        for j, value in enumerate(row):
            if value == Stats.Player_X:
                x = square_positions[i * 3 + j][0] + SQUARE_SIZE // 2
                y = square_positions[i * 3 + j][1] + SQUARE_SIZE // 2
                pygame.draw.line(screen, RED, (x - 20, y - 20), (x + 20, y + 20), LINE_WIDTH)
                pygame.draw.line(screen, RED, (x - 20, y + 20), (x + 20, y - 20), LINE_WIDTH)
            elif value == Stats.Player_O:
                x = square_positions[i * 3 + j][0] + SQUARE_SIZE // 2
                y = square_positions[i * 3 + j][1] + SQUARE_SIZE // 2
                pygame.draw.circle(screen, GRAY, (x, y), SQUARE_SIZE // 5, LINE_WIDTH)
            else:
                x = square_positions[i * 3 + j][0] + SQUARE_SIZE // 2
                y = square_positions[i * 3 + j][1] + SQUARE_SIZE // 2
                pygame.draw.line(screen, GREEN, (x - 20, y - 20), (x + 20, y + 20), LINE_WIDTH)
                pygame.draw.line(screen, GREEN, (x - 20, y + 20), (x + 20, y - 20), LINE_WIDTH)
                pygame.draw.circle(screen, GREEN, (x, y), SQUARE_SIZE // 5, LINE_WIDTH)


# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
DARKGREEN = (0, 100, 0)
FORESTGREEN = (34, 139, 34)
GRAY = (64, 64, 64)

# iniciando o pygame
pygame.init()

# Definindo o tamanaho da tela
screen = pygame.display.set_mode((1280, 720))

# Definindo a tela inicial

# Definindo cor de fundo
screen.fill(GREEN)

# Definindo fonte
font = pygame.font.Font(None, 36)

# Renderize o texto como uma superfície
header_surface = font.render("Jogo Da Velha", True, BLACK)

# Defina a posição da superfície
header_x = (1280 - header_surface.get_width()) // 2
header_y = 20

# Desenhe a superfície na tela
screen.blit(header_surface, (header_x, header_y))

# Atualize a tela
pygame.display.update()

# Defina as constantes para a grade
SQUARE_SIZE = 200
LINE_WIDTH = 5
NUM_SQUARES = 3

# Obtenha as dimensões da tela
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# Calcule a posição da grade no centro da tela
grid_width = NUM_SQUARES * SQUARE_SIZE
grid_height = NUM_SQUARES * SQUARE_SIZE
grid_x = (SCREEN_WIDTH - grid_width) // 2
grid_y = (SCREEN_HEIGHT - grid_height) // 2

# Defina um objeto Rect para cada retângulo do jogo da velha
rects = []
for i in range(3):
    for j in range(3):
        rect = pygame.Rect(i * SQUARE_SIZE + grid_x, j * SQUARE_SIZE + grid_y, SQUARE_SIZE, SQUARE_SIZE)
        rects.append(rect)

# Iniciando o tabuleiro do jogo
board = GameBoard()

# atualizando toda a tela
pygame.display.flip()

# Looping para inciar a tela, enquanto o usuario não clicar no botão 'X' a tela ira continuar rodando
game_over = 1

show_board(board, screen)
pygame.display.update()


# Definindo os simbolos dos jogadores
player_one = Stats.Player_X
player_two = Stats.Player_O

# Definindo a vez do jogador um
player_one_turn = True

while True:
    show_board(board, screen)
    pygame.display.update()
    moves = [((0, 0), 0), ((0, 1), 1), ((0, 2), 2), ((1, 0), 3), ((1, 1), 4), ((1, 2), 5), ((2, 0), 6),
             ((2, 1), 7), ((2, 2), 8)]
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Verifique se é a vez do jogador um
            if player_one_turn:
                # Permita que o jogador um faça uma jogada
                cont = 1
                while cont:
                    if cont == 0:
                        break
                    # Verifique se o clique do mouse está dentro de um dos retângulos
                    mouse_pos = pygame.mouse.get_pos()
                    mov_1 = -1
                    for coord, index in moves:
                        if rects[index].collidepoint(mouse_pos):
                            mov_1 = board.insert(*coord, player_one)
                            if mov_1 == -1:
                                cont = 1
                            else:
                                cont = 0
                # Muda para a vez do jogador dois
                player_one_turn = False
                show_board(board, screen)
                pygame.display.update()
            else:
                cont = 1
                while cont:
                    if cont == 0:
                        break
                    # Verifique se o clique do mouse está dentro de um dos retângulos
                    mouse_pos = pygame.mouse.get_pos()
                    mov_2 = -1
                    moves = [((0, 0), 0), ((0, 1), 1), ((0, 2), 2), ((1, 0), 3), ((1, 1), 4), ((1, 2), 5), ((2, 0), 6),
                             ((2, 1), 7), ((2, 2), 8)]

                    for coord, index in moves:
                        if rects[index].collidepoint(mouse_pos):
                            mov_2 = board.insert(*coord, player_two)
                            if mov_2 == -1:
                                cont = 1
                            cont = 0
                # Mudar para a vez do jogador um
                player_one_turn = True

                # Verificar se o jogo acabou
            if board.has_winner() != Stats.EMPTY or board.check_tie():
                winner = board.has_winner()

                if winner == player_one:
                    show_board(board, screen)
                    pygame.display.update()

                    # Criando o pop-up com tkinter
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Fim de Jogo", "Jogador 1 venceu!")
                    root.destroy()

                    # Resetando o tabuleiro
                    board = GameBoard()
                    pygame.display.update()
                    show_board(board, screen)
                    pygame.display.update()
                    print("Jogador 1 venceu!")
                elif winner == player_two:
                    show_board(board, screen)
                    pygame.display.update()

                    # Criando o pop-up com tkinter
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Fim de Jogo", "Jogador 2 venceu!")
                    root.destroy()

                    # Resetando o tabuleiro
                    board = GameBoard()
                    pygame.display.update()
                    show_board(board, screen)
                    pygame.display.update()
                    print("Jogador 2 venceu!")
                else:
                    show_board(board, screen)
                    pygame.display.update()

                    # Criando o pop-up com tkinter
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Fim de Jogo", "Empate!")
                    root.destroy()

                    # Resetando o tabuleiro
                    board = GameBoard()
                    pygame.display.update()
                    show_board(board, screen)
                    pygame.display.update()
                    print("Empate!")

                # Resetando o tabuleiro
                board = GameBoard()
                pygame.display.update()
                show_board(board, screen)
                pygame.display.update()

