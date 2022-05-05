import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 320
FRAME_RATE = 60



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
    self.window.fill((0,0,0))
    # Draw frets
    space_between = 50
    fret_width = 5
    position = 50
    frets = 0
    while frets < 13:
      pygame.draw.rect(self.window, (90, 39, 41), (position, 0, fret_width, SCREEN_HEIGHT))
      position += fret_width + space_between 
      frets += 1

    # Draw strings
    space_between = 40
    string_width = 5 # actually passed as height
    position = 40
    strings = 0
    while strings < 6:
      pygame.draw.rect(self.window, (200, 200, 200), (0, position, SCREEN_WIDTH, string_width))
      position += string_width + space_between
      strings += 1

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
