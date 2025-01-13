import pygame
import random
from subprocess import call
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
REVEAL_FONT = pygame.font.SysFont('raleway', 50)
END_FONT = pygame.font.SysFont('clearsans', 50)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

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
game_lost = False
end = False
print(target)

def reset_wordle_game():
    global word, letters, guesses, yc, game_won, game_lost, submitted_words, target
    word = ""
    letters = []
    guesses = 0
    yc = 100
    game_won = False
    game_lost = False
    submitted_words = []
    target = random.choice(load_words())
    
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
    end = False
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
            win1 = WIN_FONT.render("YOU'VE", True, GREEN)
            win2 = WIN_FONT.render("WON!", True, GREEN)
            screen.blit(win1,(20,250))
            screen.blit(win2, (575,250))
            pygame.display.update()
            end = True
            

        if guesses == 6:
            print(f"Game Over! The word was {target}.")
            result1 = WIN_FONT.render("GAME", True, RED)
            result2 = WIN_FONT.render("OVER!", True, RED)
            reveal1 = REVEAL_FONT.render("The word was", True, RED)
            reveal2 = REVEAL_FONT.render(target, True, RED)
            screen.blit(result1,(50,230))
            screen.blit(result2,(50,270))
            screen.blit(reveal1, (560,230))
            screen.blit(reveal2, (620,270))
            pygame.display.update()
            end = True
            

        if end:
            running = True  # Control variable for the end screen loop
            while running:
                pygame.draw.rect(screen, (255, 165, 0), (25, 305, 170, 120))
                pygame.draw.rect(screen, (255, 165, 0), (565, 310, 170, 120))
                pygame.draw.rect(screen, (0, 0, 139), (30, 310, 160, 110))
                pygame.draw.rect(screen, (88, 25, 52), (570, 315, 160, 110))

                TITLE_FONT.set_underline(True)
                again = TITLE_FONT.render("Play", True, WHITE)
                again2 = TITLE_FONT.render("Again", True, WHITE)
                quit = END_FONT.render("Go To", True, WHITE)
                quit2 = END_FONT.render("Main", True, WHITE)
                quit3 = END_FONT.render("Menu", True, WHITE)
                TITLE_FONT.set_underline(False)

                screen.blit(again, (60, 310))
                screen.blit(again2, (40, 365))
                screen.blit(quit, (600, 315))
                screen.blit(quit2, (605, 350))
                screen.blit(quit3, (600, 385))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        m_x, m_y = pygame.mouse.get_pos()
                        print(m_x, m_y)
                        # Check if "Play Again" button is clicked
                        if 25 <= m_x <= 195 and 305 <= m_y <= 425:
                            print("Play Again button clicked")
                            reset_wordle_game()
                            main()
                            
                        # Check if "Quit" button is clicked
                        elif 565 <= m_x <= 735 and 310 <= m_y <= 430:
                            pygame.quit()
                            call(["python", "main.py"]) 
                            running = False
                            pygame.quit()
                            exit()
                            
if __name__ == "__main__":
    main()


