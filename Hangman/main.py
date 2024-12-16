import pygame
import math
import random
import sys
import os

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('bg.jpg')
menu_bg = pygame.image.load('menu.jpg')
country = pygame.image.load('countries.png')
animals = pygame.image.load('animals.png')
food = pygame.image.load('food.png')
other = pygame.image.load('random.png')
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
win_se = pygame.mixer.Sound('win.wav')
lose_se = pygame.mixer.Sound('lose.wav')
right_se = pygame.mixer.Sound('right.wav')
wrong_se = pygame.mixer.Sound('wrong.wav')

# BG Music
pygame.mixer.music.load('bg.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(.1)

#Load Images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
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

#Main Game Variables
hangman_status = 0

guessed = []

print(images)


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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i in range(4):
                    rect = rectangles[i]
                    if rect.collidepoint(x, y):
                        with open(type[i] + ".txt", "r") as file:
                            words = file.read().splitlines()
                        running = False
                        break
    return words


words = menu()
word = random.choice(words)


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
    pygame.draw.rect(screen, BLACK, (150, 15, 500, 100))
    pygame.draw.rect(screen, YELLOW, (150, 15, 500, 100), 5)

    pygame.draw.rect(screen, BLACK, (10, 175, 780, 100))
    pygame.draw.rect(screen, YELLOW, (10, 175, 780, 100), 5)
    WIN_FONT.set_underline(True)
    text1 = WIN_FONT.render(message, 1, color)
    WIN_FONT.set_underline(False)
    text2 = LOSE_FONT.render(f"The word was {word}", 1, RED)
    if hangman_status == 6:
        lose_se.play()
        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2,
                            HEIGHT / 5 - text1.get_height()))
        screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2,
                            HEIGHT / 2 - text2.get_height()))
    elif won:
        win_se.play()
        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2,
                            HEIGHT / 2 - text1.get_height()))

    pygame.draw.rect(screen, BLUE, (225, 350, 350, 100))
    pygame.draw.rect(screen, BLACK, (225, 350, 350, 100), 5)
    button = pygame.Rect(225, 350, 350, 100)
    TITLE_FONT.set_underline(True)
    again = TITLE_FONT.render("Play Again", 1, WHITE)
    screen.blit(again, (275, 370))
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
                    pygame.quit()
                    os.execl(sys.executable, sys.executable, *sys.argv)
                else:
                    pygame.quit()
                    quit()

def main():
    global hangman_status
    FPS = 60
    clock = pygame.time.Clock()
    run = True
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
        draw()
        global won
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


if __name__ == "__main__":
    main()
    