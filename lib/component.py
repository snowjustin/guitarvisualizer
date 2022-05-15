import pygame
import lib.constants as constants



class Component:
  def __init__(self, state, position):
    self.state = state
    self.position = position

  def render(self, surface):
    raise(NotImplementedError())



class Button(Component):
  def __init__(self, state, position, button_text):
    super().__init__(state, position)
    self.text = button_text
    self.active = False

  
  def set_active_state(self, state):
    self.active = state


  def render(self, surface):
    if self.active:
      button_color = text_color = constants.BUTTON_ACTIVE
    else:
      button_color = text_color = constants.BUTTON_INACTIVE

    if self.position.collidepoint(pygame.mouse.get_pos()):
      mouse_hover = 0
      text_color = surface.get_at((0, 0)) # this allows us to use the background
                                                # color of the main window to create hover effect
    else:
      mouse_hover = 5

    cb_font = pygame.font.Font(constants.FONT_PATH, constants.BUTTON_FONT_SIZE)
    cb_button = pygame.draw.rect(surface, button_color, self.position, mouse_hover, constants.BUTTON_CORNER_RADIUS)
    cb_surf = cb_font.render(self.text, True, text_color)
    cb_rect = cb_surf.get_rect(center=cb_button.center)
    surface.blit(cb_surf, cb_rect)



class Fretboard(Component):
  def __init__(self, state, position):
    super().__init__(state, position)
    self.note_positions = []

  def render(self, surface):
    # Setup the fretboard
    x_origin, y_origin = self.position.left, self.position.top
    width = self.position.width
    height = self.position.height
    max_frets = self.state.guitar.get_number_of_frets()
    max_strings = len(self.state.guitar.strings)
    fretboard = pygame.Surface((width, height))
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

    if constants.DEBUG_MODE:
      pygame.draw.rect(fretboard, constants.RED, fretboard.get_rect(), 1)  
    surface.blit(fretboard, (x_origin, y_origin))

    # Draw notes
    self.note_positions = []
    x_spacing = (width // max_frets)
    y_spacing = (height // max_strings)
    x = x_origin + (x_spacing // 2)
    y = y_origin
    note_radius = int(y_spacing // 2.25)
    guitar_strings = self.state.guitar.get_strings()
    notefont = pygame.font.Font(constants.FONT_PATH, constants.NOTE_FONT_SIZE)

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



class TextArea(Component):
  def __init__(self, state, position, text, textcolor, bgcolor):
    super().__init__(state, position)
    self.textcolor = textcolor
    self.bgcolor = bgcolor
    self.text = text

  def render(self, surface, text=None):
    if text is not None:
      self.text = text
    ta_font = pygame.font.Font(constants.FONT_PATH, constants.TEXT_FONT_SIZE)
    ta_area = pygame.draw.rect(surface, self.bgcolor, self.position)
    ta_surf = ta_font.render(self.text, True, self.textcolor)
    x, y = ta_area.midleft
    ta_rect = ta_surf.get_rect(midleft=(x + 5, y))
    surface.blit(ta_surf, ta_rect)

