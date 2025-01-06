import pygame

pygame.init()

# Create Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('Game Centre/Connect 4/bg2.jpg')
grid = pygame.image.load('Game Centre/Connect 4/grid.png')

# Fonts and Colours
TITLE_FONT = pygame.font.SysFont('Raleway', 65)
LABEL_FONT = pygame.font.SysFont('comicsans', 40)
STATUS_FONT = pygame.font.SysFont('Raleway', 35)
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
x_positions = [225, 283, 342, 400, 459, 517, 575]
y_positions = [180, 235, 290, 345, 400, 455]
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
    title_text = TITLE_FONT.render("Connect 4", True, (200,150,100))
    screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 0))
    TITLE_FONT.set_underline(False)

    # Display Instrunctions
    instructions = INSTRUCTIONS_FONT.render(
        "Press 1-7 to drop your piece in a column", True, (200,150,150))
    screen.blit(instructions, (WIDTH / 2 - instructions.get_width() / 2, 80))

    # Display Column Labels
    for i in range(7):
        label = LABEL_FONT.render(str(i + 1), True, (255,255,0))
        screen.blit(label, (x_positions[i] - label.get_width() // 2, 90))

    # Display Grid
    screen.blit(grid, (175, 140))

    # Draws Circles where spaces have been chosen/occupied
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            if taken[row][col]:
                color = COLORS[taken[row][col] - 1]
                pygame.draw.circle(screen, color, positions[row][col], 21)

    # Check if any player has won
    if not won:
        players = ["RED'S", "YELLOW'S"]
        turn_text = players[player]  
        turn_action = "TURN"         

        if player == 0:
            x_pos = 40  
        else:
            x_pos = 625  

        y_start = 240  
        line_spacing = 35  

        player_render = STATUS_FONT.render(turn_text, True, COLORS[player])
        screen.blit(player_render, (x_pos, y_start))

        turn_render = STATUS_FONT.render(turn_action, True, COLORS[player])
        turn_x_pos = x_pos + (player_render.get_width() // 2) - (turn_render.get_width() // 2)  # Center "TURN"
        screen.blit(turn_render, (turn_x_pos, y_start + line_spacing))

    elif won:
        players = ["RED'S", "YELLOW'S"]
        winner_text = players[player]
        win_action = "WINS!"

        if player == 0:
            x_pos = 40
        else:
            x_pos = 625

        y_start = 240
        line_spacing = 35

        STATUS_FONT.set_bold(True)
        STATUS_FONT.set_underline(True)

        winner_render = STATUS_FONT.render(winner_text, True, COLORS[player])
        screen.blit(winner_render, (x_pos, y_start))

        win_render = STATUS_FONT.render(win_action, True, COLORS[player])

        winner_width = winner_render.get_width()
        win_width = win_render.get_width()

        win_x_pos = x_pos + (winner_width // 2) - (win_width // 2)

        screen.blit(win_render, (win_x_pos, y_start + line_spacing))

        STATUS_FONT.set_bold(False)
        STATUS_FONT.set_underline(False)

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
            if taken[r][c] == p and taken[r + 1][c] == p and taken[r + 2][c] == p and taken[r + 3][c] == p:
                return True

    # Checks the Diagonal winning of bottom left to top right
    for r in range(3):
        for c in range(4):
            if taken[r][c] == p and taken[r + 1][c + 1] == p and taken[r + 2][c + 2] == p and taken[r + 3][c + 3] == p:
                return True

    # Checks the diagonal winning of bottom right to top left
    for r in range(3, 6):
        for c in range(4):
            if taken[r][c] == p and taken[r - 1][c + 1] == p and taken[r - 2][c + 2] == p and taken[r - 3][c + 3] == p:
                return True
    return False


# Main Game Loop
def main():
    global player, won
    screen.fill((255, 200, 20))
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        draw(won)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

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
                        return  # Exit the game after a win
                    player = 1 - player  # Switch player

# Start the game loop
while True:
    main()