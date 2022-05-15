import pygame
import pygame.gfxdraw
import lib.guitar as guitar
import lib.component as component
import lib.constants as constants



class UserInterface:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption(constants.APP_TITLE)
    self.clock = pygame.time.Clock()
    self.running = True
    self.state = AppState()
    # UI components
    self.build_chord_button = component.Button(self.state, pygame.Rect(20, 20, 150, 40), constants.BUILD_CHORD_BUTTON_TEXT)
    self.fretboard_ui = component.Fretboard(self.state, pygame.Rect(20, 90, 760, 280))
    self.key_picker_button = component.Button(self.state, pygame.Rect(200, 20, 150, 40), "Pick Key")
    self.chord_info = component.TextArea(self.state, pygame.Rect(360, 20, 150, 20), "Chord Info", constants.BLACK, constants.WHITE)
    self.key_info = component.TextArea(self.state, pygame.Rect(360, 40, 150, 20), "Key Info", constants.BLACK, constants.WHITE)
    status_bar_rect = pygame.Rect(0, constants.SCREEN_HEIGHT - 20, constants.SCREEN_WIDTH, 20)
    self.status_bar = component.TextArea(self.state, status_bar_rect, self.state.status_message, constants.GREEN, constants.GRAY)


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
          if self.build_chord_button.position.collidepoint(event.pos) and not self.state.picking_key:
            self.state.building_chord = not self.state.building_chord
            self.build_chord_button.set_active_state(self.state.building_chord)
            if self.state.building_chord: 
              self.state.status_message = "Building a chord..."
            else:
              self.state.status_message = ""

          elif self.key_picker_button.position.collidepoint(event.pos) and not self.state.building_chord:
            self.state.picking_key = not self.state.picking_key
            self.key_picker_button.set_active_state(self.state.picking_key)
            if self.state.picking_key: 
              self.state.status_message = "Picking a key..."
            else:
              self.state.status_message = ""

          elif self.state.building_chord:
            for note in self.fretboard_ui.note_positions:
              if note["pos"].collidepoint(event.pos):
                self.state.update(note["note"])


  def render(self):
    self.window.fill(constants.WHITE)
    self.build_chord_button.render(self.window)
    self.fretboard_ui.render(self.window)
    self.key_picker_button.render(self.window)
    self.chord_info.render(self.window)
    self.key_info.render(self.window)
    self.status_bar.render(self.window, self.state.status_message)
    pygame.display.update()


  def run(self):
    while self.running:
      self.process_input()
      self.render()
      self.clock.tick(constants.FRAME_RATE)



class AppState():
  def __init__(self):
    self.guitar = guitar.Guitar()
    self.building_chord = False
    self.picking_key = False
    self.active_chord = []
    self.status_message = ""

  def update(self, note):
    if self.building_chord:
      if note in self.active_chord:
        self.active_chord.remove(note)
      else:
        if len(self.active_chord) < constants.MAX_ACTIVE_NOTES:  # temp circumstance to only allow 5 chord notes at a maximum.
          self.active_chord.append(note)



if __name__ == "__main__":
  a = UserInterface()
  a.run()
  pygame.quit()
