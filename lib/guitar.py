import lib.note as note

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
  def __init__(self, fret_count=13):
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
        
      for x in range(fret_count):
        notes.append(n.copy())
        n.increment(1)

      self.strings[k] = notes

  
  def change_string_tuning(self, string_pos, semitones, tuning_direction):
    """This function allows you to change the tuning of one string of the guitar."""
    if tuning_direction not in [TUNE_UP, TUNE_DOWN]:
      raise(InvalidTunigException)
    elif string_pos not in self.strings.keys():
      raise(InvalidStringPositionException)
    elif not isinstance(semitones, int):
      raise(TypeError('invalid data type for int'))

    for n in self.strings[string_pos]:
      if tuning_direction == TUNE_UP:
        n.increment(semitones)
      else:
        n.decrement(semitones)

  
  def get_note(self, string_number, fret):
      if string_number not in self.strings.keys():
        raise(InvalidStringPositionException)
      elif fret > self.get_number_of_frets() or fret < 1:
        raise(InvalidFretPosition)
      else:
        return self.strings[string_number][fret - 1]


  def get_number_of_frets(self):
    return len(self.strings[STRING_1])


  def get_number_of_strings(self):
    return len(self.strings)


  def get_strings(self):
    return list(self.strings)



class InvalidTunigException(Exception):
  def __str__(self):
    return('invalid value for tuning, must be either value TUNE_UP or TUNE_DOWN')



class InvalidStringPositionException(Exception):
  def __str__(self):
    return('invalid value for string position')



class InvalidFretPosition(Exception):
  def __str__(self):
    return(f'invalid fret position. Must be a value between 1 and ')
