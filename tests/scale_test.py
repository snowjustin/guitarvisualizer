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

  def test_notecount(self):
    s = scale.Scale(scale.MAJOR, note.Note())
    self.assertEqual(s.notecount(), 8)

  def test_getdegree(self):
    # These test's will only ever work with 7 note scales.
    s = scale.Scale(scale.MAJOR, note.Note())
    self.assertEqual(s.getdegree(scale.TONIC).note, note.N_C)
    self.assertEqual(s.getdegree(scale.SUPERTONIC).note, note.N_D)
    self.assertEqual(s.getdegree(scale.MEDIANT).note, note.N_E)
    self.assertEqual(s.getdegree(scale.SUBDOMINANT).note, note.N_F)
    self.assertEqual(s.getdegree(scale.DOMINANT).note, note.N_G)
    self.assertEqual(s.getdegree(scale.SUBMEDIANT).note, note.N_A)
    self.assertEqual(s.getdegree(scale.LEADINGTONE).note, note.N_B)
    self.assertEqual(s.getdegree(8).note, note.N_C)
    self.assertEqual(s.getdegree(9).note, note.N_D)

if __name__ == "__main__":
  unittest.main()
