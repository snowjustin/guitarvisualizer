import app.note as note

# Constants for different standard western scales based on semitone or wholetone differences.
# Seven note scales/modes
SCALES
IONIAN_SCALE = [note.TONE, note.TONE, note.SEMITONE, note.TONE, note.TONE, note.TONE, note.SEMITONE]
DORIAN_SCALE = [note.TONE, note.SEMITONE, note.TONE, note.TONE, note.TONE, note.SEMITONE, note.TONE]
PHRYGIAN_SCALE = [note.SEMITONE, note.TONE, note.TONE, note.TONE, note.SEMITONE, note.TONE, note.TONE]
LYDIAN_SCALE = [note.TONE, note.TONE, note.TONE, note.SEMITONE, note.TONE, note.TONE, note.SEMITONE]
MIXOLYDIAN_SCALE = [note.TONE, note.TONE, note.SEMITONE, note.TONE, note.TONE, note.SEMITONE, note.TONE]
AEOLIAN_SCALE = [note.TONE, note.SEMITONE, note.TONE, note.TONE, note.SEMITONE, note.TONE, note.TONE]
LOCRIAN_SCALE = [note.SEMITONE, note.TONE, note.TONE, note.SEMITONE, note.TONE, note.TONE, note.TONE]

# Five note scales
MAJOR_PENTATONIC = [note.TONE, note.TONE, note.SEMITONE*3, note.TONE, note.SEMITONE*3]
MINOR_PENTATONIC = [note.SEMITONE*3, note.TONE, note.TONE, note.SEMITONE*3, note.TONE]

# Whole tone six note scale
WHOLE_TONE = [note.TONE, note.TONE, note.TONE, note.TONE, note.TONE, note.TONE]

# Constant Scale Names
IONIAN = "ionian"
DORIAN = "dorian"
PHRYGIAN = "phrygian"
LYDIAN = "lydian"
MIXOLYDIAN = "mixolydian"
AEOLIAN = "aeolian"
LOCRIAN = "locrian"
MAJOR = "major"  # same as ionian scale
MINOR = "minor"  # same as aeolian scale
MAJOR_PEN = "major-pen"
MINOR_PEN = "minor-pen"
WHOLE = "whole"

# Supported scales
SUPPORTED_SCALES = {
  IONIAN: IONIAN_SCALE,
  DORIAN: DORIAN_SCALE,
  PHRYGIAN: PHRYGIAN_SCALE,
  LYDIAN: LYDIAN_SCALE,
  MIXOLYDIAN: MIXOLYDIAN_SCALE,
  AEOLIAN: AEOLIAN_SCALE,
  LOCRIAN: LOCRIAN_SCALE,
  MAJOR: IONIAN_SCALE,
  MINOR: AEOLIAN_SCALE,
  MAJOR_PEN: MAJOR_PENTATONIC,
  MINOR_PEN: MINOR_PENTATONIC,
  WHOLE: WHOLE_TONE
}

class Scale:
  def __init__(self, name):
    if name not in SUPPORTED_SCALES.keys():
      raise InvalidScaleName
    else:
      pass

    
class InvalidScaleNameException(Exception):
  def __init__(self):
    pass

  def __str__(self):
    return "Scale objects must use a supported scale: see scale.SUPPORTED_SCALES for a list"