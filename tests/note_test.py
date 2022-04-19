import unittest
import app.note as note



class TestNoteClass(unittest.TestCase):
  def test_init(self):
    # Test default parameter
    n = note.Note(note.N_A)
    self.assertEqual(n.note, note.N_A)
    self.assertEqual(n.octave, 1)

    # Test passed octave
    n = note.Note(note.N_B, 2)
    self.assertEqual(n.octave, 2)

  def test_increment(self):
    n = note.Note(note.N_A, 2)
    n.increment(11)
    self.assertEqual(n.note, note.N_A_FLAT)
    self.assertEqual(n.octave, 2)
    n.increment(1)
    self.assertEqual(n.note, note.N_A)
    self.assertEqual(n.octave, 3)
    n.increment(12)
    self.assertEqual(n.note, note.N_A)
    self.assertEqual(n.octave, 4)

  def test_decrement(self):
    n = note.Note(note.N_A, 4)
    n.decrement(1)
    self.assertEqual(n.note, note.N_A_FLAT)
    self.assertEqual(n.octave, 3)
    n.decrement(1)
    self.assertEqual(n.note, note.N_G)
    self.assertEqual(n.octave, 3)
    n.decrement(12)
    self.assertEqual(n.note, note.N_G)
    self.assertEqual(n.octave, 2)
    

  def test_copy(self):
    a = note.Note(note.N_D_FLAT)
    b = a.copy()
    self.assertEqual(a.note, b.note)
    self.assertEqual(a.octave, b.octave)
    self.assertNotEqual(a, b)

if __name__ == "__main__":
  unittest.main()