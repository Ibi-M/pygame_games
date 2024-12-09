import pygame
import random
pygame.init()

# Creating the Window
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('wordle/bg.jpg')
pygame.display.set_caption("Wordle")

# Fonts and Colors
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
LETTER_FONT = pygame.font.SysFont('sansserif', 80)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)

# Global variable for user input
word = ""
letters = []
words = ("hello", "words")
target = random.choice(words).upper()
print(target)

def submit(word):
    if word == target:
        print("Great!")
        for letter in word:
            update = LETTER_FONT.render(letter)

def draw():
    global xc
    global word, letters  # Access global variables
    screen.fill((0, 0, 0))
    
    # Display Title
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("Wordle", True, WHITE)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    # Draw the grid
    for row in range(6):  # 6 rows
        for col in range(5):  # 5 columns
            x = 140 + col * 70
            y = 150 + row * 70
            pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 70, 70), width=3)

    # Display the word
    xc = 150
    yc = 160
    column = 0
    for l in letters:
        letter = LETTER_FONT.render(l,True,WHITE)
        x = xc + (column * 70)
        y = yc
        screen.blit(letter,(x,y))
        column = column + 1

    pygame.display.update()

def main():
    global LETTER_FONT
    global word, letters  # Access global variables
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(word) > 0:  # Ensure word is not empty
                        word = word[:-1]
                        if letters:  # Ensure letters list is not empty
                            letters.pop()
                elif event.key == pygame.K_RETURN and len(word) == 5:
                    if word == target:
                        submit(word)
                elif event.unicode.isalpha():
                    if len(word) >= 5:
                        print("Limit!")
                    else:
                        word += event.unicode.upper()  # Append the typed character
                        letters.append(event.unicode.upper())  # Add only the new letter
     
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
