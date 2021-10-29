import unittest
import note



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
    n = note.Note(note.N_A)
    n.increment(1)
    self.assertEqual(n.note, note.N_A_SHARP)
    self.assertEqual(n.octave, 1)

    n = note.Note(note.N_G_SHARP)
    n.increment(1)
    self.assertEqual(n.note, note.N_A)
    self.assertEqual(n.octave, 2)

  def test_decrement(self):
    n = note.Note(note.N_A_SHARP)
    n.decrement(1)
    self.assertEqual(n.note, note.N_A)
    self.assertEqual(n.octave, 1)

    n = note.Note(note.N_A, 3)
    n.decrement(1)
    self.assertEqual(n.note, note.N_A_FLAT)
    self.assertEqual(n.octave, 2)

  def test_copy(self):
    a = note.Note(note.N_D_FLAT)
    b = a.copy()
    self.assertEqual(a.note, b.note)
    self.assertEqual(a.octave, b.octave)
    self.assertNotEqual(a, b)

if __name__ == "__main__":
  unittest.main()