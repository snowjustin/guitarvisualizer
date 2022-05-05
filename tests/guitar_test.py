import unittest
import app.guitar as guitar
import app.note as note

class TestGuitarClass(unittest.TestCase):
  def test_init(self):
    g = guitar.Guitar()
    self.assertEqual(g.strings[1][0].note, note.N_E)
    self.assertEqual(g.strings[1][0].octave, 2)
    self.assertEqual(g.strings[1][12].note, note.N_E)
    self.assertEqual(g.strings[1][12].octave, 3)



  def test_change_string_tuning(self):
    g = guitar.Guitar()
    self.assertEqual(g.strings[guitar.STRING_3][0].note, note.N_D)
    self.assertEqual(g.strings[guitar.STRING_3][0].octave, 3)

    g.change_string_tuning(guitar.STRING_3, 4, guitar.TUNE_UP)
    self.assertEqual(g.strings[guitar.STRING_3][0].note, note.N_F_SHARP)
    self.assertEqual(g.strings[guitar.STRING_3][0].octave, 3)

    self.assertRaises(TypeError, g.change_string_tuning, guitar.STRING_3, 'garbage data', guitar.TUNE_UP)
    self.assertRaises(guitar.InvalidTunigException, g.change_string_tuning, guitar.STRING_3, 3, 'garbage data')
    self.assertRaises(guitar.InvalidStringPositionException, g.change_string_tuning, 'garbage data', 3, guitar.TUNE_UP)

if __name__ == "__main__":
  unittest.main()
