import unittest
import lib.note as note

# When used frequencies were pulled from https://pages.mtu.edu/~suits/notefreqs.html as a resource


class TestNoteClass(unittest.TestCase):
  def test_init(self):
    # Test thrown exceptions
    self.assertRaises(note.InvalidNoteException, note.Note, 'garbage data', 2)
    self.assertRaises(TypeError, note.Note, note.N_A, 'garbage data')

    # Test default parameter
    n = note.Note()
    self.assertEqual(n.note, note.N_C)
    self.assertEqual(n.octave, 4)
    self.assertEqual(n.frequency, 261.63)

    # Test passed octave
    n = note.Note(note.N_B, 2)
    self.assertEqual(n.note, note.N_B)
    self.assertEqual(n.octave, 2)
    self.assertEqual(n.frequency, 123.47)

  def test_increment(self):
    n = note.Note(note.N_C, 2)
    n.increment(11)
    self.assertEqual(n.note, note.N_B)
    self.assertEqual(n.octave, 2)
    n.increment(1)
    self.assertEqual(n.note, note.N_C)
    self.assertEqual(n.octave, 3)
    n.increment(12)
    self.assertEqual(n.note, note.N_C)
    self.assertEqual(n.octave, 4)

  def test_decrement(self):
    n = note.Note(note.N_C, 4)
    n.decrement(1)
    self.assertEqual(n.note, note.N_B)
    self.assertEqual(n.octave, 3)
    n.decrement(1)
    self.assertEqual(n.note, note.N_B_FLAT)
    self.assertEqual(n.octave, 3)
    n.decrement(12)
    self.assertEqual(n.note, note.N_B_FLAT)
    self.assertEqual(n.octave, 2)
    

  def test_copy(self):
    a = note.Note(note.N_D_FLAT)
    b = a.copy()
    self.assertEqual(a.note, b.note)
    self.assertEqual(a.octave, b.octave)
    self.assertNotEqual(a, b)

if __name__ == "__main__":
  unittest.main()