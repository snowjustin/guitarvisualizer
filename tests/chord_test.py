import unittest
import lib.chord as chord
import lib.note as note

class TestChordClass(unittest.TestCase):
  def test_init(self):
    c = chord.Chord(note.Note())
    self.assertEqual(c.root.note, note.N_C)
    self.assertRaises(TypeError, chord.Chord, "garbage data")
    self.assertRaises(TypeError, chord.Chord, note.Note(), "garbage data")

if __name__ == "__main__":
  unittest.main()
