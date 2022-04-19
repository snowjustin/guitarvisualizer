import unittest
import app.scale as scale
import app.note as note

class TestScaleClass(unittest.TestCase):
  def test_init(self):
    tonic = note.Note()
    self.assertRaises(scale.InvalidNoteException, scale.Scale, scale.AEOLIAN, 'garbage data')
    self.assertRaises(scale.InvalidScaleNameException, scale.Scale, 'garbage data', tonic)
    
    s = scale.Scale(scale.MAJOR, tonic)
    self.assertEqual(len(s.scale), 8)
    self.assertEqual(s.scale[0].note, note.N_C)
    self.assertEqual(s.scale[0].octave, 4)
    self.assertEqual(s.scale[1].note, note.N_D)
    self.assertEqual(s.scale[1].octave, 4)
    self.assertEqual(s.scale[2].note, note.N_E)
    self.assertEqual(s.scale[2].octave, 4)
    self.assertEqual(s.scale[3].note, note.N_F)
    self.assertEqual(s.scale[3].octave, 4)
    self.assertEqual(s.scale[4].note, note.N_G)
    self.assertEqual(s.scale[4].octave, 4)
    self.assertEqual(s.scale[5].note, note.N_A)
    self.assertEqual(s.scale[5].octave, 4)
    self.assertEqual(s.scale[6].note, note.N_B)
    self.assertEqual(s.scale[6].octave, 4)
    self.assertEqual(s.scale[7].note, note.N_C)
    self.assertEqual(s.scale[7].octave, 5)

if __name__ == "__main__":
  unittest.main()
