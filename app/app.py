import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 320
FRAME_RATE = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class App:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Guitar Visualizer")
    self.clock = pygame.time.Clock()
    self.running = True


  def process_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        break
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.running = False
          break


  def update(self):
    pass


  def render(self):
    self.window.fill(WHITE)

    # Setup the fretboard
    width = SCREEN_WIDTH - 40
    height = SCREEN_HEIGHT - 40
    string_width = 2
    self.fretboard = pygame.Surface((width, height - 40))
    self.fretboard.fill(WHITE)
    
    # Draw strings
    space_between = height // 6
    position = 0
    strings = 0
    while strings < 6:
      ref_rect = pygame.draw.rect(self.fretboard, BLACK, (0, position, (width // 12) * 12, string_width))
      position += space_between
      strings += 1

    # Draw frets
    space_between = width // 12
    position = 0
    frets = 0
    pygame.draw.rect(self.fretboard, BLACK, (position, 0, string_width * 2, ref_rect.bottom))
    position += space_between
    while frets < 12:
      pygame.draw.rect(self.fretboard, BLACK, (position, 0, string_width, ref_rect.bottom))
      position += space_between
      frets += 1

    # Draw notes
    self.window.blit(self.fretboard, (20,20))
    pygame.display.update()


  def run(self):
    while self.running:
      self.process_input()
      self.update()
      self.render()
      self.clock.tick(FRAME_RATE)


app = App()
app.run()
pygame.quit()
