## Note Constants
SEMITONE = 1
TONE = 2

# Notes
N_A = "A"
N_A_SHARP = "A#/Bb"
N_B_FLAT = N_A_SHARP
N_B = "B"
N_C = "C"
N_C_SHARP = "C#/Db"
N_D_FLAT = N_C_SHARP
N_D = "D"
N_D_SHARP = "D#/Eb"
N_E_FLAT = N_D_SHARP
N_E = "E"
N_F = "F"
N_F_SHARP = "F#/Gb"
N_G_FLAT = N_F_SHARP
N_G = "G"
N_G_SHARP = "G#/Ab"
N_A_FLAT = N_G_SHARP
NOTES = [N_A, N_A_SHARP, N_B, N_C, N_C_SHARP, N_D,  N_D_SHARP, N_E, N_F, N_F_SHARP, N_G, N_G_SHARP]


class Note:
  def __init__(self, note, octave=1):
    self.note = note
    self.octave = octave

    
  def increment(self, n_semitones):
    if self.note == N_G_SHARP:
      self.note = NOTES[0]
      self.octave += 1
    else:
      self.note = NOTES[NOTES.index(self.note) + (SEMITONE * n_semitones)]
      

  def decrement(self, n_semitones):
    if self.note == N_A:
      self.note = NOTES[len(NOTES) - 1]
      self.octave -= 1
    else:
      self.note = NOTES[NOTES.index(self.note) - (SEMITONE * n_semitones)]
      

  def copy(self):
    return Note(self.note, self.octave)
