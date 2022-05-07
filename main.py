import pygame
import pygame.gfxdraw
import lib.guitar as guitar
import pathlib

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FRAME_RATE = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
NOTE_COLOR = WHITE #(25, 255, 25)

FONT_PATH = pathlib.Path('font/Share-Regular.ttf')

class UserInterface:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Guitar Visualizer")
    self.clock = pygame.time.Clock()
    self.running = True
    self.state = AppState()
    self.build_chord = Button(self.state, pygame.Rect(20, 20, 150, 40), "Build Chord")
    self.build_chord_clicked = False


  def process_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        break
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.running = False
          break
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: # left button
          if self.build_chord.location.collidepoint(pygame.mouse.get_pos()):
            self.state.building_chord = not self.state.building_chord


  def update(self):
    pass


  def render(self):
    self.window.fill(WHITE)
    # Setup the buttons you can use in the game.
    self.build_chord.render(self.window)

    # Setup the fretboard
    x_origin, y_origin = 20, 90
    width = 760
    height = 280
    max_frets = self.state.guitar.get_number_of_frets()
    max_strings = len(self.state.guitar.strings)
    self.fretboard = pygame.Surface((width, height - 40))
    self.fretboard.fill(WHITE)
    
    # Draw strings
    space_between = height // max_strings
    position = 0
    strings = 0
    string_width = fret_width = 2
    string_length = (width // max_frets) * max_frets
    while strings < max_strings:
      ref_rect = pygame.draw.rect(self.fretboard, BLACK, (0, position, string_length, string_width))
      position += space_between
      strings += 1

    # Draw frets
    space_between = width // max_frets
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
    note_radius = int(y_spacing // 2.25)
    guitar_strings = self.state.guitar.get_strings()
    notefont = pygame.font.Font(FONT_PATH, 24)

    for fret in range(1, max_frets + 1):
      # draw notes
      for string_p in reversed(guitar_strings):
        n_img = pygame.draw.circle(self.window, GRAY, (x, y), note_radius)
        if n_img.collidepoint(pygame.mouse.get_pos()):
          pygame.draw.circle(self.window, BLACK, (x, y), note_radius, string_width)
        active_note = self.state.guitar.get_note(string_p, fret)
        active_note_surf = notefont.render(active_note.__str__(), True, NOTE_COLOR)
        active_note_rect = active_note_surf.get_rect(center=n_img.center)
        self.window.blit(active_note_surf, active_note_rect)
        y += y_spacing

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
    self.building_chord = False
    


class Button():
  def __init__(self, state_tracker, location, button_text):
    self.state = state_tracker
    self.location = location
    self.text = button_text

  def render(self, surface):
    # Setup the buttons you can use in the game.
    if self.state.building_chord:
      button_color = text_color = (25, 25, 225)
    else:
      button_color = text_color = BLACK

    if self.location.collidepoint(pygame.mouse.get_pos()):
      mouse_hover = 0
      text_color = WHITE
    else:
      mouse_hover = 5

    cb_font = pygame.font.Font(FONT_PATH, 26)
    cb_button = pygame.draw.rect(surface, button_color, self.location, mouse_hover, 4)
    cb_surf = cb_font.render(self.text, True, text_color)
    cb_rect = cb_surf.get_rect(center=cb_button.center)
    surface.blit(cb_surf, cb_rect)   

if __name__ == "__main__":
  a = UserInterface()
  a.run()
  pygame.quit()
