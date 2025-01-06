import pygame
import math
import random
import sys
import os

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('Game Centre/Hangman/bg.jpg')
menu_bg = pygame.image.load('Game Centre/Hangman/menu.jpg')
country = pygame.image.load('Game Centre/Hangman/countries.png')
animals = pygame.image.load('Game Centre/Hangman/animals.png')
food = pygame.image.load('Game Centre/Hangman/food.png')
other = pygame.image.load('Game Centre/Hangman/random.png')
pygame.display.set_caption("Hangman")
state = ""

# Fonts and Colors
LABEL_FONT = pygame.font.SysFont('aharoni', 35)
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
TITLE_FONT = pygame.font.SysFont('sansserif', 70)
WIN_FONT = pygame.font.SysFont('sansserif', 100)
LOSE_FONT = pygame.font.SysFont('sansserif', 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

# Sound Effects
win_se = pygame.mixer.Sound('Game Centre/Hangman/win.wav')
lose_se = pygame.mixer.Sound('Game Centre/Hangman/lose.wav')
right_se = pygame.mixer.Sound('Game Centre/Hangman/right.wav')
wrong_se = pygame.mixer.Sound('Game Centre/Hangman/wrong.wav')

# BG Music
pygame.mixer.music.load('Game Centre/Hangman/bg.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(.1)

# Load Images
images = []
for i in range(7):
    image = pygame.image.load("Game Centre/Hangman/hangman" + str(i) + ".png")
    images.append(image)

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Game Variables
hangman_status = 0
guessed = []

def menu():
    screen.blit(menu_bg, (0, 0))
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("HANGMAN", True, YELLOW)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    RECT_SIZE = 170
    GAP = 40  # Gap between rectangles

    # Calculate the total width of the rectangles and gap
    total_width = 2 * RECT_SIZE + GAP

    # Calculate X positions for centering
    rect_x1 = (WIDTH - total_width) // 2
    rect_x2 = rect_x1 + RECT_SIZE + GAP

    rect_y_top = 100
    rect_y_bottom = rect_y_top + RECT_SIZE + 40

    rectangles = []

    rect1_top = pygame.Rect(rect_x1, rect_y_top, RECT_SIZE, RECT_SIZE)
    rectangles.append(rect1_top)
    pygame.draw.rect(screen, YELLOW, rect1_top)
    pygame.draw.rect(screen, RED, rect1_top, 5)

    rect2_top = pygame.Rect(rect_x2, rect_y_top, RECT_SIZE, RECT_SIZE)
    rectangles.append(rect2_top)
    pygame.draw.rect(screen, YELLOW, rect2_top)
    pygame.draw.rect(screen, RED, rect2_top, 5)

    rect1_bottom = pygame.Rect(rect_x1, rect_y_bottom, RECT_SIZE, RECT_SIZE)
    rectangles.append(rect1_bottom)
    pygame.draw.rect(screen, YELLOW, rect1_bottom)
    pygame.draw.rect(screen, RED, rect1_bottom, 5)

    rect2_bottom = pygame.Rect(rect_x2, rect_y_bottom, RECT_SIZE, RECT_SIZE)
    rectangles.append(rect2_bottom)
    pygame.draw.rect(screen, YELLOW, rect2_bottom)
    pygame.draw.rect(screen, RED, rect2_bottom, 5)

    screen.blit(country, (230, 130))
    screen.blit(animals, (235, 360))
    screen.blit(food, (440, 160))
    screen.blit(other, (450, 365))

    LABEL_FONT.set_underline(True)
    countries = LABEL_FONT.render("COUNTRIES", True, BLACK)
    screen.blit(countries, (220, 110))
    animal = LABEL_FONT.render("ANIMALS", True, BLACK)
    screen.blit(animal, (235, 330))
    foods = LABEL_FONT.render("FOODS", True, BLACK)
    screen.blit(foods, (460, 120))
    others = LABEL_FONT.render("RANDOM", True, BLACK)
    screen.blit(others, (445, 330))
    pygame.display.update()

    type = ["countries", "foods", "animals", "random"]
    print ("Got here line 128")
    running = True
    print ("Got here 2")
    while running:
        print ("Got here 3")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print ("I have detetected a mouse click ")
                x, y = pygame.mouse.get_pos()

                print("I got here")
                for i in range(4):
                    rect = rectangles[i]
                    if rect.collidepoint(x, y):
                        with open('Game Centre/Hangman/'+ type[i] + ".txt", "r") as file:
                            words = file.read().splitlines()
                        running = False
                        break
    return words

def reset_game():
    global hangman_status, guessed, word, letters
    hangman_status = 0
    guessed = []
    word = random.choice(menu())  # Choose a new word
    for letter in letters:
        letter[3] = True  # Make all the letter buttons visible again
    pygame.mixer.music.play(-1, 0.0)  # Restart the music
    print("Game reset and music restarted")
    main()

def draw():
    global bg
    screen.blit(bg, (0, 0))

    # Draw Title
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("HANGMAN", True, YELLOW)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    # Draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, YELLOW)
    screen.blit(text, (350, 200))

    #Draw Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, WHITE, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, WHITE)
            screen.blit(text,
                        (x - text.get_width() / 2, y - text.get_height() / 2))

    screen.blit(images[hangman_status], (50, 100))
    pygame.display.update()

def display_message(message, result, color):
    pygame.time.delay(2000)
    screen.blit(bg, (0, 0))

    WIN_FONT.set_underline(True)
    text1 = WIN_FONT.render(message, 1, color)
    WIN_FONT.set_underline(False)
    text2 = LOSE_FONT.render(f"The word was {word}", 1, RED)
    if hangman_status == 6:
        pygame.draw.rect(screen, BLACK, (150, 15, 500, 100))
        pygame.draw.rect(screen, YELLOW, (150, 15, 500, 100), 5)
        pygame.draw.rect(screen, BLACK, (10, 175, 780, 100))
        pygame.draw.rect(screen, YELLOW, (10, 175, 780, 100), 5)
        lose_se.play()
        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2,
                            HEIGHT / 5 - text1.get_height()))
        screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2,
                            HEIGHT / 2 - text2.get_height()))
    elif won:
        pygame.draw.rect(screen, BLACK, (150, 130, 500, 100))
        pygame.draw.rect(screen, YELLOW, (150, 130, 500, 100), 5)
        win_se.play()
        screen.blit(text1, (220, 145))

    if won:
        y_c = 275
    else:
        y_c = 350
    pygame.draw.rect(screen, BLUE, (225, y_c, 350, 100))
    pygame.draw.rect(screen, BLACK, (225, y_c, 350, 100), 5)
    button = pygame.Rect(225, y_c, 350, 100)
    TITLE_FONT.set_underline(True)
    again = TITLE_FONT.render("Play Again", 1, WHITE)
    screen.blit(again, (275, y_c + 20))
    TITLE_FONT.set_underline(False)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if button.collidepoint(x, y):
                    reset_game()  # Reset the game instead of quitting
                    return  # Exit the message function and continue the game loop

def main():
    global hangman_status, won, word
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    word = random.choice(menu())  # Choose a word from the menu
    while run:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                wrong_se.play()
                                hangman_status += 1
                            else:
                                right_se.play()
            if event.type == pygame.KEYDOWN:
                allowed = [
                    pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e,
                    pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j,
                    pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o,
                    pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t,
                    pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y,
                    pygame.K_z
                ]
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        if letter == event.key:
                            letter[3] = False
                            guessed.append(ltr)

        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            pygame.mixer.music.stop()
            display_message("You WON!", "win", GREEN)
            break

        if hangman_status == 6:
            pygame.mixer.music.stop()
            display_message("You LOST!", "lost", RED)
            break

#if __name__ == "__main__":
 #   main()

main()