import pygame
from gameBoard import GameBoard, Stats

import tkinter as tk
from tkinter import messagebox

import pickle

SCREEN_SIZE = (1280, 720)

# Dicionario
stats = {"player_one_wins": 0, "player_two_wins": 0, "draws": 0}


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

# Home Screen
# O tamanho da tela vai ser o mesmo do que o do jogo

# Definindo o botão para jogar

# -> Definir a posição do botão
button_x = (1280 / 2) - (200 / 2)
button_y = (720 / 2) - (50 / 2)

# -> Definir o retângulo do botão
button_rect = pygame.Rect(button_x, button_y, 200, 50)

# -> Criar o texto do botão
font = pygame.font.Font(None, 36)
text = font.render("Jogar", True, BLACK)

# Definindo o botão para ver historico de jogos

# -> Definir a posição do botão
button_x1 = (1280 / 2) - (200 / 2)
button_y1 = (1000 / 2) - (50 / 2)

# -> Definir o retângulo do botão
button_rect_hist = pygame.Rect(button_x1, button_y1, 200, 50)

# -> Criar o texto do botão
font1 = pygame.font.Font(None, 36)
text1 = font.render("Historico", True, BLACK)

# Resetando o arquivo
with open("stats.bin", "wb") as f:
    pickle.dump(stats, f)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Definindo fonte
    font = pygame.font.Font(None, 100)

    # Renderize o texto como uma superfície
    header_surface = font.render("Jogo Da Velha", True, BLACK)

    # Defina a posição da superfície
    header_x = (1280 - header_surface.get_width()) // 2
    header_y = 60

    # Defininfo a cor de fundo
    screen.fill(FORESTGREEN)

    pygame.draw.rect(screen, DARKGREEN, (0, 0, 1280, 200))

    pygame.draw.rect(screen, WHITE, (button_x-52, button_y-52, 304, 304))

    pygame.draw.rect(screen, GRAY, (button_x-50, button_y-50, 300, 300))

    # Desenhando a superfície na tela
    screen.blit(header_surface, (header_x, header_y))

    # Desenhando o botão na tela
    pygame.draw.rect(screen, WHITE, button_rect)
    screen.blit(text, (button_x + 60, button_y + 10))

    # Desenhando o botão na tela
    pygame.draw.rect(screen, WHITE, button_rect_hist)
    screen.blit(text1, (button_x1 + 50, button_y1 + 10))

    # Verificando se o botão do mouse foi pressionado
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            # Definindo a tela do jogo
            # Definindo cor de fundo
            screen.fill(GREEN)

            # Definindo fonte
            font = pygame.font.Font(None, 36)

            # Renderizando o texto como uma superfície
            header_surface = font.render("Jogo Da Velha", True, BLACK)

            # Definindo a posição da superfície
            header_x = (1280 - header_surface.get_width()) // 2
            header_y = 20

            # Desenhando a superfície na tela
            screen.blit(header_surface, (header_x, header_y))

            # Atualizando a tela
            pygame.display.update()

            # Definindo as constantes para a grade
            SQUARE_SIZE = 200
            LINE_WIDTH = 5
            NUM_SQUARES = 3

            # Obtendo as dimensões da tela
            screen_info = pygame.display.Info()
            SCREEN_WIDTH = screen_info.current_w
            SCREEN_HEIGHT = screen_info.current_h

            # Calculando a posição da grade no centro da tela
            grid_width = NUM_SQUARES * SQUARE_SIZE
            grid_height = NUM_SQUARES * SQUARE_SIZE
            grid_x = (SCREEN_WIDTH - grid_width) // 2
            grid_y = (SCREEN_HEIGHT - grid_height) // 2

            # Definindo um objeto Rect para cada retângulo do jogo da velha
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

            running = True
            while running:
                show_board(board, screen)
                pygame.display.update()
                moves = [((0, 0), 0), ((0, 1), 1), ((0, 2), 2), ((1, 0), 3), ((1, 1), 4), ((1, 2), 5), ((2, 0), 6),
                         ((2, 1), 7), ((2, 2), 8)]

                # Definindo fonte
                f = pygame.font.Font(None, 24)

                button = pygame.Rect(40, 660, 85, 50)

                text3 = f.render("Home", True, BLACK)

                # Desenhando o botão na tela
                pygame.draw.rect(screen, WHITE, button)

                screen.blit(text3, (60, 680))

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if button.collidepoint(mouse):
                            running = False
                        # Verificando se é a vez do jogador um
                        elif player_one_turn:
                            # Permita que o jogador um faça uma jogada
                            cont = 1
                            while cont:
                                if cont == 0:
                                    break
                                # Verificando se o clique do mouse está dentro de um dos retângulos
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
                                # Verificando se o clique do mouse está dentro de um dos retângulos
                                mouse_pos = pygame.mouse.get_pos()
                                mov_2 = -1
                                moves = [((0, 0), 0), ((0, 1), 1), ((0, 2), 2), ((1, 0), 3), ((1, 1), 4), ((1, 2), 5),
                                         ((2, 0), 6),
                                         ((2, 1), 7), ((2, 2), 8)]

                                for coord, index in moves:
                                    if rects[index].collidepoint(mouse_pos):
                                        mov_2 = board.insert(*coord, player_two)
                                        if mov_2 == -1:
                                            cont = 1
                                        cont = 0
                            # Mudar para a vez do jogador um
                            player_one_turn = True

                            # Verificando se o jogo acabou
                        if board.has_winner() != Stats.EMPTY or board.check_tie():
                            winner = board.has_winner()

                            if winner == player_one:
                                stats["player_one_wins"] += 1

                                # Salva as estatísticas em um arquivo binário
                                with open("stats.bin", "wb") as f:
                                    pickle.dump(stats, f)

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
                                stats["player_two_wins"] += 1

                                # Salva as estatísticas em um arquivo binário
                                with open("stats.bin", "wb") as f:
                                    pickle.dump(stats, f)

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
                                stats["draws"] += 1

                                # Salva as estatísticas em um arquivo binário
                                with open("stats.bin", "wb") as f:
                                    pickle.dump(stats, f)

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

        elif button_rect_hist.collidepoint(mouse_pos):
            with open("stats.bin", "rb") as f:
                run = True
                while run:
                    for even in pygame.event.get():
                        if even.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif pygame.mouse.get_pressed()[0]:
                            mouse_pos2 = pygame.mouse.get_pos()
                            if button.collidepoint(mouse_pos2):
                                run = False  # saia do loop quando o botão "Home" é clicado

                    try:
                        stats = pickle.load(f)
                    except EOFError:
                        continue

                    # Definindo fonte
                    font = pygame.font.Font(None, 24)

                    qtd_player_1 = stats["player_one_wins"]
                    qtd_player_2 = stats["player_two_wins"]
                    qtd_draw = stats["draws"]

                    text3 = font.render("Home", True, BLACK)

                    button = pygame.Rect(40, 660, 85, 50)

                    # Definindo a tela do historico
                    # Definindo fonte
                    font = pygame.font.Font(None, 100)

                    # Renderize o texto como uma superfície
                    header_surface = font.render("Historico", True, BLACK)

                    # Defina a posição da superfície
                    header_x = (1280 - header_surface.get_width()) // 2
                    header_y = 60

                    # Defininfo a cor de fundo
                    screen.fill(GREEN)

                    pygame.draw.rect(screen, DARKGREEN, (0, 0, 1280, 200))

                    pygame.draw.rect(screen, WHITE, (button_x - 52, button_y - 52, 304, 304))

                    pygame.draw.rect(screen, GRAY, (button_x - 50, button_y - 50, 300, 300))

                    # Desenhando o botão na tela
                    pygame.draw.rect(screen, WHITE, button)

                    screen.blit(text3, (60, 680))

                    # Desenhe a superfície na tela
                    screen.blit(header_surface, (header_x, header_y))

                    font = pygame.font.Font(None, 36)

                    text2 = font.render(f"Jogador X: {qtd_player_1}", True, BLACK)
                    screen.blit(text2, (button_x + 25, button_y + 30))
                    text2 = font.render(f"Jogador 0: {qtd_player_2}", True, BLACK)
                    screen.blit(text2, (button_x + 25, button_y + 70))
                    text2 = font.render(f"Empate: {qtd_draw}", True, BLACK)
                    screen.blit(text2, (button_x + 25, button_y + 110))

                    pygame.display.update()

    # Atualizar a tela
    pygame.display.update()
