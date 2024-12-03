import pygame
import math
import random

pygame.init()

# Create Window
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = pygame.image.load('grid.jpg')

# Fonts & Colors
TITLE_FONT = pygame.font.SysFont('sansserif', 70)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Sizes
DEFAULT_IMAGE_SIZE = (50, 50)

# Define labels globally
labels = ["1", "2", "3", "4", "5", "6", "7"]


def draw():
    screen.blit(grid, (100, 150))
    TITLE_FONT.set_underline(True)
    text = TITLE_FONT.render("Connect 4", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
    TITLE_FONT.set_underline(False)

    coor = 50
    count = 71
    for label in labels:
        coor = coor + count
        circle_center = (coor + 20, 120)
        pygame.draw.circle(screen, BLACK, circle_center, 30, 3)
        text = TITLE_FONT.render(label, True, BLACK)
        screen.blit(text, (circle_center[0] - text.get_width() // 2,
                           circle_center[1] - text.get_height() // 2))

    red = pygame.image.load('red.png')
    yellow = pygame.image.load('yellow.png')
    red = pygame.transform.scale(red, DEFAULT_IMAGE_SIZE)
    yellow = pygame.transform.scale(yellow, DEFAULT_IMAGE_SIZE)
    screen.blit(red, (115, 175))
    screen.blit(yellow, (415, 175))

    pygame.display.update()


def main():
    global labels
    screen.fill((255, 200, 200))
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    x_offset = 50
    spacing = 71
    circle_centers = [(x_offset + spacing * (i + 1) + 20, 120)
                      for i in range(len(labels))]

    while run:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for i in range(len(circle_centers)):
                    c_x, c_y = circle_centers[i]
                    dis = math.sqrt((c_x - m_x)**2 + (c_y - m_y)**2)

                    if dis <= 30:
                        print(f"Clicked on {labels[i]}")
                        if i == 0:
                            screen.blit

    pygame.quit()


while True:
    main()
    pygame.quit()
