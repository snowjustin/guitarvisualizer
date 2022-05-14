import pygame
import pygame.gfxdraw
import lib.guitar as guitar
import lib.component as component
import lib.constants as constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FRAME_RATE = 60



class UserInterface:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Guitar Visualizer")
    self.clock = pygame.time.Clock()
    self.running = True
    self.state = AppState()
    # UI components
    self.build_chord_button = component.Button(self.state, pygame.Rect(20, 20, 150, 40), "Build Chord")
    self.fretboard_ui = Fretboard(self.state, pygame.Rect(20, 90, 760, 280))
    # TODO: add status bar to guide user
    # TODO: add component for showing selected chord.


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
          if self.build_chord_button.position.collidepoint(event.pos):
            self.state.building_chord = not self.state.building_chord
          elif self.state.building_chord and self.fretboard_ui.position.collidepoint(event.pos):
            for note in self.fretboard_ui.note_positions:
              if note["pos"].collidepoint(event.pos):
                self.state.update(note["note"])


  def render(self):
    self.window.fill(constants.WHITE)
    self.build_chord_button.render(self.window)
    self.fretboard_ui.render(self.window)
    pygame.display.update()


  def run(self):
    while self.running:
      self.process_input()
      self.render()
      self.clock.tick(FRAME_RATE)



class AppState():
  def __init__(self):
    self.guitar = guitar.Guitar()
    self.building_chord = False
    self.active_chord = []

  def update(self, note):
    if self.building_chord:
      if note in self.active_chord:
        self.active_chord.remove(note)
      else:
        if len(self.active_chord) < 5:  # temp circumstance to only allow 5 chord notes at a maximum.
          self.active_chord.append(note)



class Fretboard():
  def __init__(self, state, position):
    self.state = state
    self.position = position
    self.note_positions = []

  def render(self, surface):
    # Setup the fretboard
    x_origin, y_origin = self.position.left, self.position.top
    width = self.position.width
    height = self.position.height
    max_frets = self.state.guitar.get_number_of_frets()
    max_strings = len(self.state.guitar.strings)
    fretboard = pygame.Surface((width, height - 40))
    fretboard.fill(constants.WHITE)
    
    # Draw strings
    space_between = height // max_strings
    position = 0
    strings = 0
    string_width = fret_width = 2
    string_length = (width // max_frets) * max_frets
    while strings < max_strings:
      ref_rect = pygame.draw.rect(fretboard, constants.BLACK, (0, position, string_length, string_width))
      position += space_between
      strings += 1

    # Draw frets
    space_between = width // max_frets
    position = 0
    frets = 0
    pygame.draw.rect(fretboard, constants.BLACK, (position, 0, fret_width * 2, ref_rect.bottom))
    position += space_between
    while frets < max_frets:
      pygame.draw.rect(fretboard, constants.BLACK, (position, 0, fret_width, ref_rect.bottom))
      position += space_between
      frets += 1

    surface.blit(fretboard, (x_origin, y_origin))

    # Draw notes
    self.note_positions = []
    x_spacing = (width // max_frets)
    y_spacing = (height // max_strings)
    x = x_origin + (x_spacing//2)
    y = y_origin
    note_radius = int(y_spacing // 2.25)
    guitar_strings = self.state.guitar.get_strings()
    notefont = pygame.font.Font(constants.FONT_PATH, 24)

    for fret in range(1, max_frets + 1):
      # draw notes
      for string_p in reversed(guitar_strings):
        current_note = self.state.guitar.get_note(string_p, fret)
        if current_note in self.state.active_chord:
          n_img = pygame.draw.circle(surface, constants.NOTE_COLORS[self.state.active_chord.index(current_note)], (x, y), note_radius)
        else:
          note_found = False
          for n in self.state.active_chord:
            if n.note == current_note.note:
              n_img = pygame.draw.circle(surface, constants.NOTE_COLORS_SECONDARY[self.state.active_chord.index(n)], (x, y), note_radius)
              note_found = True
              break
          if not note_found:
            n_img = pygame.draw.circle(surface, constants.GRAY, (x, y), note_radius)
        if n_img.collidepoint(pygame.mouse.get_pos()):
          pygame.draw.circle(surface, constants.BLACK, (x, y), note_radius, string_width)
        active_note = self.state.guitar.get_note(string_p, fret)
        active_note_surf = notefont.render(active_note.__str__(), True, constants.NOTE_COLOR)
        active_note_rect = active_note_surf.get_rect(center=n_img.center)
        surface.blit(active_note_surf, active_note_rect)
        y += y_spacing
        self.note_positions.append({
          "pos": n_img,  # we store the rect for the circle since it is bigger than that of the letters being draw for the notes.
          "note": active_note
        })

      y = y_origin
      x += x_spacing



if __name__ == "__main__":
  a = UserInterface()
  a.run()
  pygame.quit()
