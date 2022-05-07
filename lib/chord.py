import lib.note as note
 


class Chord:
  def __init__(self, rootnote, *notes):
    if not isinstance(rootnote, note.Note):
      raise(TypeError("Chord objects require a Note object to be passed as the root note of the chord."))
    else:
      for n in notes:
        if not isinstance(n, note.Note):
          raise(TypeError("Chord objects only accept Note objects for initialization."))

      self.root = rootnote
      self.notes = [rootnote] # storing the root note here will need to be remembered if we ever wish
                              # to make changes to chord in the future.
      for n in notes:
        self.notes.append(n)
      self.notes.sort(key=lambda n: n.frequency)