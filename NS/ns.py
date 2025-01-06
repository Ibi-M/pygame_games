import pygame

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('Game Centre/NS/bg3.jpg')
x = pygame.image.load('Game Centre/NS/x.png')
nought = pygame.image.load('Game Centre/NS/nought.png')

players = [nought,x]
player = 0

pygame.display.set_caption("Noughts and Crosses")

# Fonts and Colors
TITLE_FONT = pygame.font.SysFont('comicsans', 65)
CROSS_FONT = pygame.font.SysFont('comicsans', 200)
TURN_FONT = pygame.font.SysFont('raleway', 35, bold = True)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
taken = []

cell_size = 120  # Adjust this value based on your image size

board = [[(210, 105), (340, 105), (470, 105)],
         [(210, 235), (340, 235), (470, 235)],
         [(210, 365), (340, 365), (470, 365)]]


for i in range(3):
    row = [False] * 3
    taken.append(row)

won = False

rectangles = []

def check_win():
    # Check horizontal lines for a win
    for row in range(3):
        if taken[row][0] == taken[row][1] == taken[row][2] and taken[row][0] != False:
            return True

    # Check vertical lines for a win
    for col in range(3):
        if taken[0][col] == taken[1][col] == taken[2][col] and taken[0][col] != False:
            return True

    # Check diagonal (top-left to bottom-right)
    if taken[0][0] == taken[1][1] == taken[2][2] and taken[0][0] != False:
        return True

    # Check diagonal (top-right to bottom-left)
    if taken[0][2] == taken[1][1] == taken[2][0] and taken[0][2] != False:
        return True
    


    return False

def draw():
    screen.blit(bg, (0, 0))
    # Display Title
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("Noughts & Crosses", True, YELLOW)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 0))
    TITLE_FONT.set_underline(False)

    start_x = 205
    start_y = 100
    rect_width = 130
    rect_height = 130
    spacing = 130

    # Draw the grid and store rectangle positions
    for row in range(3):
        for col in range(3):
            rect_x = start_x + col * spacing
            rect_y = start_y + row * spacing
            rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
            rectangles.append((rectangle, row, col))  
            pygame.draw.rect(screen, (255, 255, 255), rectangle, 3)

    # Display current player move
    for row in range(3):
        for col in range(3):
            if taken[row][col]:
                screen.blit(players[taken[row][col] - 1], board[row][col])

    turn_text = "TURN"

    left_text = "NOUGHT'S" 
    if player == 0:
        left_turn = TURN_FONT.render(left_text, True, WHITE)
        turn = TURN_FONT.render(turn_text, True, WHITE)
        screen.blit(left_turn, (10, HEIGHT / 2 - left_turn.get_height() / 2))
        screen.blit(turn, (50, (HEIGHT / 2 - left_turn.get_height() / 2) + 40))

    # Right side (Cross's turn)
    right_text = "CROSS'S" 
    if player == 1:
        right_turn = TURN_FONT.render(right_text, True, WHITE)
        turn = TURN_FONT.render(turn_text, True, WHITE)
        screen.blit(right_turn, (625, HEIGHT / 2 - right_turn.get_height() / 2))
        screen.blit(turn, (645, (HEIGHT / 2 - right_turn.get_height() / 2) + 40))
        

    pygame.display.update()

def main():
    global player, won
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
                x, y = pygame.mouse.get_pos()
                for rect, row, col in rectangles:
                    if rect.collidepoint(x, y) and not taken[row][col] and not won:
                        taken[row][col] = player + 1  # Mark the cell
                        if check_win():
                            won = True
                            print(f"Player {player + 1} wins!")
                        player = 1 - player  # Switch player

    pygame.quit()

if __name__ == "__main__":
    main()
