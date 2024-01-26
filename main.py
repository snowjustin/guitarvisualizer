import pygame
import pygame.gfxdraw
from mingus.containers import NoteContainer
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
    self.chord_info = component.TextArea(self.state, pygame.Rect(200, 20, 150, 20), self.state.active_chord_status, constants.BLACK, constants.WHITE)
    self.chord_name = component.TextArea(self.state, pygame.Rect(200, 40, 150, 20), self.state.active_chord_name, constants.BLACK, constants.WHITE)
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
          if self.build_chord_button.position.collidepoint(event.pos):
            self.state.building_chord = not self.state.building_chord
            self.build_chord_button.set_active_state(self.state.building_chord)
            if self.state.building_chord: 
              self.state.status_message = constants.BUILD_CHORD_STATUS_TEXT
            else:
              self.state.status_message = ""
              self.state.active_chord = NoteContainer()
              self.active_chord_status = "Notes Selected:"

          elif self.state.building_chord:
            for note in self.fretboard_ui.note_positions:
              if note["pos"].collidepoint(event.pos):
                self.state.update(note["note"])


  def render(self):
    self.window.fill(constants.WHITE)
    self.build_chord_button.render(self.window)
    self.fretboard_ui.render(self.window)
    self.chord_info.render(self.window, self.state.active_chord_status)
    self.chord_name.render(self.window, self.state.active_chord_name)
    self.status_bar.render(self.window, self.state.status_message)
    pygame.display.update()


  def run(self):
    while self.running:
      self.process_input()
      self.render()
      self.clock.tick(constants.FRAME_RATE)



class AppState():
  def __init__(self):
    self.guitar = constants.DEFAULT_GUITAR
    self.building_chord = False
    self.active_chord = NoteContainer()
    self.active_chord_status = "Notes Selected:"
    self.active_chord_name = "Name: "
    self.status_message = ""
    


  def update(self, note):
    if self.building_chord:
      if note in self.active_chord:
        self.active_chord.remove_note(note)
      else:
        if len(self.active_chord) < constants.MAX_ACTIVE_NOTES and note not in self.active_chord:
          self.active_chord.add_note(note)
    self.active_chord_status = "Notes Selected:"
    if len(self.active_chord):
      for note in self.active_chord:
        self.active_chord_status += " " + str(note).strip("'") + ","
      self.active_chord_status = self.active_chord_status[:-1]
      self.active_chord_name = "Name: " + str(self.active_chord.determine(True))



if __name__ == "__main__":
  a = UserInterface()
  a.run()
  pygame.quit()
