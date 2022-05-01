import unittest
import app.chord as chord
import app.note as note

class TestChordClass(unittest.TestCase):
  def test_init(self):
    c = chord.Chord(note.Note())
    self.assertEqual(c.root.note, note.N_C)

if __name__ == "__main__":
  unittest.main()
