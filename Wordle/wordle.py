import pygame
import random

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
line = pygame.image.load('Game Centre/Wordle/line.png')
pygame.display.set_caption("Wordle")

# Fonts and Colors
TITLE_FONT = pygame.font.SysFont('clearsans', 70)
WIN_FONT = pygame.font.SysFont('raleway', 70, bold = True)
LETTER_FONT = pygame.font.SysFont('sansserif', 80)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

def load_words():
    with open("Game Centre/Wordle/words.txt", "r") as file:
        words = file.read().splitlines()
    return words

# Global variables
xc = 230
yc = 100
word = ""
guesses = 0
letters = []
submitted_words = []  # Stores submitted words and their colors
words = load_words()
target = random.choice(words)
game_won = False  # Flag to track if the game is won
print(target)

def submit(word):
    global guesses, yc, game_won
    row_colors = []  # Store colors for each letter in the submitted word

    # Check each letter in the submitted word
    for i in range(5):  # Fixed length of the word is 5
        char = word[i]
        if char == target[i]:
            row_colors.append(GREEN)  # Correct position
        elif char in target:
            row_colors.append(YELLOW)  # Correct letter, wrong position
        else:
            row_colors.append(GRAY)  # Incorrect letter

    # Check if the word is completely correct
    if row_colors == [GREEN, GREEN, GREEN, GREEN, GREEN]:
        game_won = True

    # Append the word and its colors to the submitted_words list
    submitted_words.append((word, row_colors))
    yc += 70  # Move to the next row
    guesses += 1
    return guesses

def draw():
    global yc, xc

    screen.fill((0, 0, 0))
    screen.blit(line, (0, 70))

    # Display Title
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("WORDLE", True, WHITE)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    # Draw the grid
    for row in range(6):  # 6 rows
        for col in range(5):  # 5 columns
            x = 220 + col * 70
            y = 90 + row * 70
            pygame.draw.rect(screen, GRAY, pygame.Rect(x, y, 60, 60), width=3)

    # Display submitted words
    for row_idx in range(len(submitted_words)):
        submitted_word, row_colors = submitted_words[row_idx]
        for i in range(5):  # Word length is always 5
            char = submitted_word[i]
            color = row_colors[i]
            letter = LETTER_FONT.render(char, True, color)
            x = xc + i * 70
            y = 100 + row_idx * 70
            screen.blit(letter, (x, y))

    # Display current typing word
    for i in range(len(letters)):
        char = letters[i]
        letter = LETTER_FONT.render(char, True, WHITE)
        x = xc + i * 70
        y = yc
        screen.blit(letter, (x, y))

    if game_won:
        won = WIN_FONT.render("YOU'VE WON!", True, GREEN)
        screen.blit(won,(400,500))
    pygame.display.update()

def main():
    global word, letters, game_won
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
                    submit(word)  # Submit the word
                    word = ""  # Reset the word
                    letters = []  # Clear the letters list
                elif event.unicode.isalpha():
                    if len(word) < 5:
                        word += event.unicode.upper()  # Append the typed character
                        letters.append(event.unicode.upper())  # Add to letters list

        draw()

        if game_won:
            print("Well done!")
            draw()
            pygame.time.delay(2000)
            pygame.quit()
            break

        if guesses == 6:
            print(f"Game Over! The word was {target}.")
            pygame.time.delay(2000)
            pygame.quit()
            break

if __name__ == "__main__":
    main()
