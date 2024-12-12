import pygame

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('bg3.jpg')
grid = pygame.image.load('grid3.png')
x = pygame.image.load('cross.png')
nought = pygame.image.load('nought.png')
pygame.display.set_caption("Noughts and Crosses")

# Fonts and Colors
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
CROSS_FONT = pygame.font.SysFont('comicsans', 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
taken = []

# Define cell size
cell_size = 120  # Adjust this value based on your image size

board = [[(130, 210), (260, 210), (390, 210)],
         [(130, 340), (260, 340), (390, 340)],
         [(130, 470), (260, 470), (390, 470)]]


for i in range(3):
    row = [False] * 3
    taken.append(row)

won = False


def win(p):
    pass


def draw():
    screen.blit(bg, (0, 0))
    screen.blit(grid, (120, 200))
    # Display Title
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("Noughts & Crosses", True, YELLOW)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    # Nought and Cross
    screen.blit(x, (260, 470))
    screen.blit(nought, (260, 470))

    pygame.display.update()


def main():
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
                print(x, y)
                # Check which cell was clicked
                for row in range(3):
                    for col in range(3):
                        cell_x, cell_y = board[row][col]
                        



while True:
    main()
