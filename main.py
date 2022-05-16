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
    self.key_picker_button = component.Button(self.state, pygame.Rect(200, 20, 150, 40), constants.PICK_KEY_BUTTON_TEXT)
    self.chord_info = component.TextArea(self.state, pygame.Rect(360, 20, 150, 20), self.state.active_chord_status, constants.BLACK, constants.WHITE)
    self.key_info = component.TextArea(self.state, pygame.Rect(360, 40, 150, 20), self.state.active_key_status, constants.BLACK, constants.WHITE)
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
              self.state.status_message = constants.BUILD_CHORD_STATUS_TEXT
            else:
              self.state.status_message = ""
              self.state.active_chord = []
              self.state.active_chord_status = "Chord:"

          elif self.key_picker_button.position.collidepoint(event.pos) and not self.state.building_chord:
            self.state.picking_key = not self.state.picking_key
            self.key_picker_button.set_active_state(self.state.picking_key)
            if self.state.picking_key: 
              self.state.status_message = constants.PICK_KEY_STATUS_TEXT
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
    self.chord_info.render(self.window, self.state.active_chord_status)
    self.key_info.render(self.window, self.state.active_key_status)
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
    self.active_chord_status = "Chord:"
    self.status_message = ""
    self.active_key = None
    self.active_key_status = "Key:"


  def update(self, note):
    if self.building_chord:
      if note in self.active_chord:
        self.active_chord.remove(note)
      else:
        active_notes = list(map(lambda n: n.note, self.active_chord))
        if len(self.active_chord) < constants.MAX_ACTIVE_NOTES and note.note not in active_notes:
          self.active_chord.append(note)
    self.active_chord_status = "Chord:"
    if self.active_chord:      
      for note in self.active_chord:
        self.active_chord_status += " " + str(note)



if __name__ == "__main__":
  a = UserInterface()
  a.run()
  pygame.quit()
