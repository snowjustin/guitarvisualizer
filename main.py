import pygame
import lib.guitar as guitar

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 320
FRAME_RATE = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)


class MainApp:
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
    x_origin, y_origin = 30, 30
    width = SCREEN_WIDTH - 40
    height = SCREEN_HEIGHT - 40
    max_frets = 12
    max_strings = 6
    self.fretboard = pygame.Surface((width, height - 40))
    self.fretboard.fill(WHITE)
    
    # Draw strings
    space_between = height // 6
    position = 0
    strings = 0
    string_width = fret_width = 2
    string_length = (width // max_frets) * max_frets
    while strings < max_strings:
      ref_rect = pygame.draw.rect(self.fretboard, BLACK, (0, position, string_length, string_width))
      position += space_between
      strings += 1

    # Draw frets
    space_between = width // 12
    position = 0
    frets = 0
    pygame.draw.rect(self.fretboard, BLACK, (position, 0, fret_width * 2, ref_rect.bottom))
    position += space_between
    while frets < max_frets:
      pygame.draw.rect(self.fretboard, BLACK, (position, 0, fret_width, ref_rect.bottom))
      position += space_between
      frets += 1

    self.window.blit(self.fretboard, (x_origin, y_origin))

    # Draw notes
    x_spacing = (width // max_frets)
    y_spacing = (height // max_strings)
    x = x_origin + (x_spacing//2)
    y = y_origin
    note_radius = 20
    for j in range(max_frets):
      # draw notes
      for i in range(max_strings):
        pygame.draw.circle(self.window, GRAY, (x, y), note_radius)
        y += y_spacing
      # update variables
      y = y_origin
      x += x_spacing
    
    
    pygame.display.update()


  def run(self):
    while self.running:
      self.process_input()
      self.update()
      self.render()
      self.clock.tick(FRAME_RATE)



class AppState():
  def __init__(self):
    self.guitar = guitar.Guitar()
    



a = MainApp()
a.run()
pygame.quit()
