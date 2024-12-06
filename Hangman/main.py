import pygame
import math
import random

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('bg.jpg')
pygame.display.set_caption("Hangman")

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
TITLE_FONT = pygame.font.SysFont('sansserif', 70)
WIN_FONT = pygame.font.SysFont('sansserif', 100)
LOSE_FONT = pygame.font.SysFont('sansserif', 80)

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


# Load Words
def load_words():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return words


#Main Game Variables
hangman_status = 0
words = load_words()
word = random.choice(words)
guessed = []

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

print(images)


def draw():
    global bg
    screen.blit(bg, (0, 0))

    # Draw Title
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("HANGMAN", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    # Draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
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


def display_message(message):
    pygame.time.delay(2000)
    screen.fill(WHITE)
    text1 = WIN_FONT.render(message, 1, BLACK)
    text2 = LOSE_FONT.render(f"The word was {word}", 1, BLACK)
    if hangman_status == 6:
        lose_se.play()
        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2,
                            HEIGHT / 6 - text1.get_height()))
        screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2,
                            HEIGHT / 2 - text2.get_height()))
    elif won:
        win_se.play()
        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2,
                            HEIGHT / 2 - text1.get_height()))
    pygame.display.update()
    pygame.time.delay(3000)


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
            display_message("You WON!")
            break

        if hangman_status == 6:
            pygame.mixer.music.stop()
            display_message("You LOST!")
            break


while True:
    main()
    pygame.quit()
