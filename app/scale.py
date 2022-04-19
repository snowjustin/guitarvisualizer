import app.note as note

# Constants for different standard western scales based on semitone or wholetone differences.
# Seven note scales/modes
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
  """A class for managing classical western scales.
  
  The intention of this class is to provide a quick way of building a
  scale of notes from a chosen scale and a tonic note.
  
  Attributes
  - name: the name of the scale
  - tonic: the tonic note of the scale
  - scale: a list of all the notes in the scale
  
  Methods
  - initialize: initializes all of the attributes"""


  def __init__(self, name, tonic):
    self.initialize(name, tonic)


  def initialize(self, name, tonic):
    if name not in SUPPORTED_SCALES.keys():
      raise InvalidScaleNameException
    elif type(tonic) != note.Note:
      raise InvalidNoteException

    self.name = name
    self.tonic = tonic.copy()
    self.scale =  [self.tonic]
    for interval in SUPPORTED_SCALES[self.name]:
      next_note = self.scale[-1].copy()
      next_note.increment(interval)
      self.scale.append(next_note)



class InvalidScaleNameException(Exception):
  def __init__(self):
    pass


  def __str__(self):
    return "Scale objects must use a supported scale from scale.SUPPORTED_SCALES"



class InvalidNoteException(Exception):
  def __init__(self):
    pass


  def __str__(self):
    return "Scale objects require a Note object to be passed as the tonic note of the scale."
