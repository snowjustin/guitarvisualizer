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

BUTTON_ACTIVE = TEAL
BUTTON_INACTIVE = BLACK
BUTTON_FONT_SIZE = 26
BUTTON_CORNER_RADIUS = 4
BUILD_CHORD_BUTTON_TEXT = "Build Chord"
BUILD_CHORD_STATUS_TEXT = "Building a chord, select up to 5 notes for the chord..."
PICK_KEY_BUTTON_TEXT = "Pick Key"
PICK_KEY_STATUS_TEXT = "Picking a key..."

TEXT_FONT_SIZE = 18

NOTE_FONT_SIZE = 24
NOTE_COLOR = WHITE
NOTE_COLORS = [PURPLE, BLUE_SKY, GREEN, RED, ORANGE]
NOTE_COLORS_SECONDARY = [PURPLE_DARK, TEAL, GREEN_DARK, RED_DARK, ORANGE_DARK]
MAX_ACTIVE_NOTES = len(NOTE_COLORS)

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
    'frets': 14
}