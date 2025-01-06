import pygame
pygame.init()

WIDTH,HEIGHT = 800,500
TITLE_FONT = pygame.font.SysFont('sansserif', 60)
screen = pygame.display.set_mode((WIDTH,HEIGHT))


def draw():
    screen.fill((255,200,150))
    TITLE_FONT.set_underline(True)
    title = TITLE_FONT.render("RPS", True, (255,255,255))
    TITLE_FONT.set_underline(False)
    pygame.draw.rect(screen, (255,122,155), (WIDTH//2 - title.get_width()//2 - 15, 5, 115, 60))
    screen.blit(title,(WIDTH//2 - title.get_width()//2,10))

    # Buttons
    pygame.draw.rect(screen,(100,200,250),(100,100,200,100))
    
    
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

if __name__ == "__main__":
    main()
    