import note

# Guitar Constants
STRING_1 = 1
STRING_2 = 2
STRING_3 = 3
STRING_4 = 4
STRING_5 = 5
STRING_6 = 6
TUNE_UP = 1
TUNE_DOWN = -1

class Guitar:
  def __init__(self):
    self.strings = {
      STRING_1: [], STRING_2: [], STRING_3: [], STRING_4: [], STRING_5: [], STRING_6: []
    }

    # Build the fretboard
    for k, notes in self.strings.items(): 
      if k == STRING_1:
        n = note.Note(note.N_E, 2)
      elif k == STRING_2:
        n = note.Note(note.N_A, 2)
      elif k == STRING_3:
        n = note.Note(note.N_D, 3)
      elif k == STRING_4:
        n = note.Note(note.N_G, 3)
      elif k == STRING_5:
        n = note.Note(note.N_B, 3)
      elif k == STRING_6:
        n = note.Note(note.N_E, 4)
        
      for x in range(13):
        notes.append(n.copy())
        n.increment(1)

      self.strings[k] = notes

  def change_string_tuning(self, string_pos, semitones, tuning_direction):
    assert(tuning_direction not in [TUNE_UP, TUNE_DOWN], "Invalid parameter for tuning_direction")
    assert(string_pos not in [STRING_1, STRING_2, STRING_3, STRING_4, STRING_5, STRING_6], "Invalid parameter for string_pos")
    assert(isinstance(semitones, int), "Invalid parameter for semitones")

    for n in self.strings[string_pos]:
      if tuning_direction == TUNE_UP:
        n.increment(semitones)
      else:
        n.decrement(semitones)

