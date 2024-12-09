import pygame

pygame.init()

# Creating the Window
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('bg3.jpg')
grid = pygame.image.load('grid3.png')
x = pygame.image.load('x.png')
pygame.display.set_caption("Noughts and Crosses")
# Fonts and Colors
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
CROSS_FONT = pygame.font.SysFont('comicsans', 200)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

nought_coors = [[(190, 270), (320, 270), (450, 270)],
                [(190, 400), (320, 400), (450, 400)],
                [(190, 530), (320, 530), (450, 530)]]

cross_coors = [[(135, 205), (265, 205), (395, 205)],
               [(135, 335), (265, 335), (395, 335)],
               [(135, 465), (265, 465), (395, 465)]]


def draw():
  screen.blit(bg, (0, 0))
  screen.blit(grid, (120, 200))
  # Display Title
  TITLE_FONT.set_underline(True)
  text = TITLE_FONT.render("Noughts & Crosses", True, YELLOW)
  screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))
  TITLE_FONT.set_underline(False)

  # Nought and Cross
  pygame.draw.circle(screen, (0, 255, 0), [450, 530], 50, 17)
  cross = CROSS_FONT.render("X", True, YELLOW)
  screen.blit(x, (395, 465))

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


while True:
  main()
