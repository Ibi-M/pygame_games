import pygame

pygame.init()

# Create Window
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('bg2.jpg')
grid = pygame.image.load('grid.png')

# Fonts and Colours
TITLE_FONT = pygame.font.SysFont('Raleway', 70)
LABEL_FONT = pygame.font.SysFont('comicsans', 60)
INSTRUCTIONS_FONT = pygame.font.SysFont('sansserif', 30)
WIN_FONT = pygame.font.SysFont('comicsans', 70, bold=True)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
COLORS = [RED, YELLOW]

# Game Variables
NUM_ROWS = 6
NUM_COLUMNS = 7
player = 0
x_positions = [155, 220, 285, 350, 415, 480, 545]
y_positions = [244, 305, 366, 427, 488, 549]
positions = []
taken = []

# Create a 2D list for positions
for i in range(NUM_ROWS):
    row = []
    for j in range(NUM_COLUMNS):
        coordinate = (x_positions[j], y_positions[i])
        row.append(coordinate)
    positions.append(row)

# Initialize taken list (all False)
for i in range(NUM_ROWS):
    row = [False] * NUM_COLUMNS
    taken.append(row)
won = False


# Function for drawing all elements of game
def draw(won):
    screen.blit(bg, (0, 0))

    # Display Title
    TITLE_FONT.set_underline(True)
    title_text = TITLE_FONT.render("Connect 4", True, BLACK)
    screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 30))
    TITLE_FONT.set_underline(False)

    # Display Instrunctions
    instructions = INSTRUCTIONS_FONT.render(
        "Press 1-7 to drop your piece in a column", True, BLACK)
    screen.blit(instructions, (WIDTH / 2 - instructions.get_width() / 2, 100))

    # Display Column Labels
    for i in range(7):
        label = LABEL_FONT.render(str(i + 1), True, BLACK)
        screen.blit(label, (x_positions[i] - label.get_width() // 2, 160))

    # Display Grid
    screen.blit(grid, (100, 200))

    # Draws Circles where spaces have been chosen/occupied
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            if taken[row][col]:
                color = COLORS[taken[row][col] - 1]
                pygame.draw.circle(screen, color, positions[row][col], 24)

    # Check if any player has won
    if not won:
        turn = TITLE_FONT.render("Player " + str(player + 1) + "'s Turn", True,
                                 COLORS[player])
        screen.blit(turn, (170, 600))
    elif won:
        WIN_FONT.set_underline(True)
        final = WIN_FONT.render(f"Player {player + 1} WINS!", True,
                                COLORS[player])
        screen.blit(final, (WIDTH / 2 - final.get_width() / 2, 630))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()
    pygame.display.update()


# Checks all winning conditions
def win(p):

    # Checks the horizontal winning
    for r in range(6):
        for c in range(4):
            if taken[r][c] == p and taken[r][c + 1] == p and taken[r][
                    c + 2] == p and taken[r][c + 3] == p:
                return True

    # Checks the vertical winning
    for c in range(7):
        for r in range(3):
            if taken[r][c] == p and taken[r + 1][c] == p and taken[
                    r + 2][c] == p and taken[r + 3][c] == p:
                return True

    # Checks the Diagonal winning of bottom left to top right
    for r in range(3):
        for c in range(4):
            if taken[r][c] == p and taken[r + 1][c + 1] == p and taken[r + 2][
                    c + 2] == p and taken[r + 3][c + 3] == p:
                return True

    # Checks the diagonal winning of bottom right to top left
    for r in range(3, 6):
        for c in range(4):
            if taken[r][c] == p and taken[r - 1][c + 1] == p and taken[r - 2][
                    c + 2] == p and taken[r - 3][c + 3] == p:
                return True
    return False


# Main Game Loop
def main():
    global player
    screen.fill((255, 200, 20))
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        global won
        clock.tick(FPS)
        draw(won)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                valid_numbers = [
                    pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                    pygame.K_6, pygame.K_7
                ]
                if event.key in valid_numbers:
                    column = event.key - pygame.K_1
                    print(
                        f"Player {player + 1} wants to drop in column {column}"
                    )

                    for row in range(NUM_ROWS - 1, -1, -1):
                        if not taken[row][column]:
                            taken[row][column] = player + 1
                            break

                    if win(player + 1):
                        print(f"Player {player + 1} WINS!")
                        won = True
                        return won
                    player = 1 - player


while True:
    main()
