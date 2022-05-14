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

  def render(self, surface):
    if self.state.building_chord:
      button_color = text_color = constants.BUTTON_ACTIVE
    else:
      button_color = text_color = constants.BUTTON_INACTIVE

    if self.position.collidepoint(pygame.mouse.get_pos()):
      mouse_hover = 0
      text_color = surface.get_at((0, 0)) # this allows us to use the background
                                                # color of the main window to create hover effect
    else:
      mouse_hover = 5

    cb_font = pygame.font.Font(constants.FONT_PATH, 26)
    cb_button = pygame.draw.rect(surface, button_color, self.position, mouse_hover, 4)
    cb_surf = cb_font.render(self.text, True, text_color)
    cb_rect = cb_surf.get_rect(center=cb_button.center)
    surface.blit(cb_surf, cb_rect)