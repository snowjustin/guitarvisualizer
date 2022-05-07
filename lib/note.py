import math

## Note Constants
SEMITONE = 1
TONE = 2

A4Hz = 440  # hertz

# Notes
N_A = "A"
N_B_FLAT = N_A_SHARP = "A#/Bb"
N_B = "B"
N_C = "C"
N_D_FLAT = N_C_SHARP = "C#/Db"
N_D = "D"
N_E_FLAT = N_D_SHARP = "D#/Eb"
N_E = "E"
N_F = "F"
N_G_FLAT = N_F_SHARP = "F#/Gb"
N_G = "G"
N_A_FLAT = N_G_SHARP = "G#/Ab"
NOTES = [N_C, N_C_SHARP, N_D,  N_D_SHARP, N_E, N_F, N_F_SHARP, N_G, N_G_SHARP, N_A, N_A_SHARP, N_B]


class Note:
  def __init__(self, note=N_C, octave=4):
    if note not in NOTES:
      raise InvalidNoteException
    if not isinstance(octave, int):
      raise TypeError("Parameter octave must be of type int")

    self.note = note
    self.octave = octave
    self.frequency = self.__calculatefrequency__()
  

  def __calculatefrequency__(self):
    distance = (self.octave - 4) * 12
    local_distance = NOTES.index(self.note) - NOTES.index(N_A)
    distance += local_distance
    return round(math.pow(2, distance / 12) * A4Hz, 2)    
  
  
  def increment(self, n_semitones):
    if n_semitones:
      if self.note == N_B:
        self.note = NOTES[0]
        self.octave += 1
      else:
        self.note = NOTES[NOTES.index(self.note) + 1]
      self.increment(n_semitones - 1)
      self.__calculatefrequency__()
      

  def decrement(self, n_semitones):
    if n_semitones:
      if self.note == N_C:
        self.note = NOTES[len(NOTES) - 1]
        self.octave -= 1
      else:
        self.note = NOTES[NOTES.index(self.note) - 1]
      self.decrement(n_semitones - 1)
      self.__calculatefrequency__()
      

  def copy(self):
    return Note(self.note, self.octave)


  def __str__(self):
    if len(self.note) > 1:
      return self.note[:2]
    else:
      return self.note

  
  def __repr__(self):
    return f'Note({self.note}, {self.octave})'



class InvalidNoteException(Exception):
  def __str__(self):
    return "Given note is not contained within the note.NOTE list."