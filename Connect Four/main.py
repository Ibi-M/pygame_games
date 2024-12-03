import pygame
pygame.init()

# Create Window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = pygame.image.load('connect four/grid.jpg')

#Fonts & Colors
TITLE_FONT = pygame.font.SysFont('sansserif', 70)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw():
    screen.blit(grid,(0,200))
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("Connect 4", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)
    labels = ["1","2","3","4","5","6"]
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

main()
