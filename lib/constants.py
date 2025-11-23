import pathlib
from mingus.extra import tunings

# General Properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FRAME_RATE = 60
APP_TITLE = "Guitar Visualizer"
DEBUG_MODE = False

# color palette used: https://flatuicolors.com/palette/es
WHITE = (247, 241, 227)
BLACK = (0, 0, 0)
GRAY = (132, 129, 122)
PURPLE = (112, 111, 211)
PURPLE_DARK = (71, 71, 135)
BLUE_SKY = (52, 172, 224)
TEAL = (34, 112, 147)
GREEN = (51, 217, 178)
GREEN_DARK = (33, 140, 116)
RED = (255, 82, 82)
RED_DARK = (179, 57, 57)
ORANGE = (255, 121, 63)
ORANGE_DARK = (205, 97, 51)
MUSTARD = (255, 177, 66)
MUSTARD_DARK = (204, 142, 53)
YELLOW = (255, 218, 121)
YELLOW_DARK = (204, 174, 98)
VIOLET = (64, 64, 122)
VIOLET_DARK = (44, 44, 84)

BUTTON_ACTIVE = TEAL
BUTTON_INACTIVE = BLACK
BUTTON_FONT_SIZE = 26
BUTTON_CORNER_RADIUS = 4
BUILD_CHORD_BUTTON_TEXT = "Build Chord"
BUILD_CHORD_STATUS_TEXT = "Building a chord..."
PICK_KEY_BUTTON_TEXT = "Pick Key"
PICK_KEY_STATUS_TEXT = "Picking a key..."

TEXT_FONT_SIZE = 18

NOTE_FONT_SIZE = 24
NOTE_COLOR = WHITE
NOTE_COLORS = [
    PURPLE, 
    BLUE_SKY, 
    GREEN, 
    RED, 
    ORANGE, 
    MUSTARD, 
    YELLOW, 
    VIOLET
]
NOTE_COLORS_SECONDARY = [
    PURPLE_DARK, 
    TEAL, 
    GREEN_DARK, 
    RED_DARK, 
    ORANGE_DARK,
    MUSTARD_DARK,
    YELLOW_DARK,
    VIOLET_DARK
]

FONT_PATH = pathlib.Path('font/Share-Regular.ttf')

# Keybinding Mappings


# Instrument constants
DEFAULT_GUITAR = {
    'instrument': tunings.get_tuning(
        instrument='guitar',
        description='standard',
        nr_of_strings=6,
        nr_of_courses=1
    ), 
    'frets': 24,
    'max_active_notes': 6
}