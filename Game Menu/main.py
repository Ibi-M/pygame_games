import pygame
from subprocess import call

pygame.init()

WIDTH, HEIGHT = 800, 500
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
COLOR = (150, 200, 205)
BLUE = (0, 0, 255)
TITLE_FONT = pygame.font.SysFont('comicsans', 55)
LABEL_FONT = pygame.font.SysFont('aharoni', 35)
bg = pygame.image.load('Game Centre/Game Menu/bg3.jpg')
hangman = pygame.image.load('Game Centre/Game Menu/hangman.png')
wordle = pygame.image.load('Game Centre/Game Menu/wordle.png')
bingo = pygame.image.load('Game Centre/Game Menu/bingo.png')
rps = pygame.image.load('Game Centre/Game Menu/rps.png')
connect4 = pygame.image.load('Game Centre/Game Menu/connect.png')
ns = pygame.image.load('Game Centre/Game Menu/ns.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

type = ["hangman", "wordle", "bingo", "rps", "connect4", "ns"]
rectangles = []


def draw():
  global rectangles
  screen.blit(bg, (0, 0))
  TITLE_FONT.set_underline(True)
  title = TITLE_FONT.render("Welcome to the Game Centre!", True, YELLOW)
  screen.blit(title, (WIDTH / 2 - title.get_width() / 2, 10))
  TITLE_FONT.set_underline(False)

  RECT_SIZE = 175
  GAP = 50  # Gap between rectangles

  # Calculate the total width of the rectangles and gap
  total_width = 3 * RECT_SIZE + GAP

  # Calculate X positions for centering
  rect_x1 = (WIDTH - total_width) // 3
  rect_x2 = rect_x1 + RECT_SIZE + GAP
  rect_x3 = rect_x2 + RECT_SIZE + GAP

  rect_y_top = 100
  rect_y_bottom = rect_y_top + RECT_SIZE + GAP

  rect1_top = pygame.Rect(rect_x1, rect_y_top, RECT_SIZE, RECT_SIZE)
  rectangles.append(rect1_top)
  pygame.draw.rect(screen, COLOR, rect1_top)
  pygame.draw.rect(screen, BLUE, rect1_top, 5)
  rectangles.append(rect1_top)

  rect2_top = pygame.Rect(rect_x2, rect_y_top, RECT_SIZE, RECT_SIZE)
  rectangles.append(rect2_top)
  pygame.draw.rect(screen, COLOR, rect2_top)
  pygame.draw.rect(screen, BLUE, rect2_top, 5)
  rectangles.append(rect2_top)

  rect3_top = pygame.Rect(rect_x3, rect_y_top, RECT_SIZE, RECT_SIZE)
  rectangles.append(rect3_top)
  pygame.draw.rect(screen, COLOR, rect3_top)
  pygame.draw.rect(screen, BLUE, rect3_top, 5)
  rectangles.append(rect3_top)

  rect1_bottom = pygame.Rect(rect_x1, rect_y_bottom, RECT_SIZE, RECT_SIZE)
  rectangles.append(rect1_bottom)
  pygame.draw.rect(screen, COLOR, rect1_bottom)
  pygame.draw.rect(screen, BLUE, rect1_bottom, 5)
  rectangles.append(rect1_bottom)

  rect2_bottom = pygame.Rect(rect_x2, rect_y_bottom, RECT_SIZE, RECT_SIZE)
  rectangles.append(rect2_bottom)
  pygame.draw.rect(screen, COLOR, rect2_bottom)
  pygame.draw.rect(screen, BLUE, rect2_bottom, 5)
  rectangles.append(rect2_bottom)

  rect3_bottom = pygame.Rect(rect_x3, rect_y_bottom, RECT_SIZE, RECT_SIZE)
  rectangles.append(rect3_bottom)
  pygame.draw.rect(screen, COLOR, rect3_bottom)
  pygame.draw.rect(screen, BLUE, rect3_bottom, 5)
  rectangles.append(rect3_bottom)

  LABEL_FONT.set_underline(True)
  countries = LABEL_FONT.render("HANGMAN", True, BLACK)
  screen.blit(countries, (95, 110))

  animal = LABEL_FONT.render("WORDLE", True, BLACK)
  screen.blit(animal, (330, 110))

  foods = LABEL_FONT.render("BINGO", True, BLACK)
  screen.blit(foods, (570, 110))

  others = LABEL_FONT.render("CONNECT 4", True, BLACK)
  screen.blit(others, (320, 330))

  rock = LABEL_FONT.render("ROCK", True, BLACK)
  paper = LABEL_FONT.render("PAPER", True, BLACK)
  scissors = LABEL_FONT.render("SCISSORS", True, BLACK)
  screen.blit(rock, (125, 330))
  screen.blit(paper, (120, 355))
  screen.blit(scissors, (105, 380))

  nought = LABEL_FONT.render("NOUGHTS", True, BLACK)
  connect = LABEL_FONT.render("AND", True, BLACK)
  crosses = LABEL_FONT.render("CROSSES", True, BLACK)
  screen.blit(nought, (550, 330))
  screen.blit(connect, (580, 355))
  screen.blit(crosses, (550, 380))

  screen.blit(hangman, (95, 137))
  screen.blit(wordle, (320, 137))
  screen.blit(bingo, (528, 122))
  screen.blit(rps, (120, 405))
  screen.blit(connect4, (330, 380))
  screen.blit(ns, (565, 405))
  pygame.display.update()


def main():
  global rectangles
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
        pygame.quit()
        if 75 < x < 250 and 100 < y < 275:
          call(["python", "Game Centre/Hangman/hangman.py"])

        if 300 < x < 475 and 100 < y < 275:
          call(["python", "Game Centre/Wordle/wordle.py"])

        if 525 < x < 700 and 100 < y < 275:
          call(["python", "bingo/bingo.py"])

        if 75 < x < 250 and 325 < y < 500:
          call(["python", "rps/rps.py"])

        if 300 < x < 475 and 325 < y < 500:
          call(["python", "Game Centre/Connect 4/connect4.py"])

        if 525 < x < 700 and 325 < y < 500:
          call(["python", "Game Centre/NS/ns.py"])

      # for i in range(6):
      #if rectangles[i].collidepoint(x, y):
      # call(["python", f"{type[i]}/{type[i]}.py"])


if __name__ == "__main__":
  main()
