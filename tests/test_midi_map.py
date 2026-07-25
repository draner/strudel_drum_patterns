import unittest
from strudel_converter.midi_map import midi_to_sample, name_to_sample, resolve_sample


class TestMidiMap(unittest.TestCase):
    def test_midi_to_sample(self):
        self.assertEqual(midi_to_sample(36), "bd")
        self.assertEqual(midi_to_sample(38), "sd")
        self.assertEqual(midi_to_sample(42), "hh")
        self.assertEqual(midi_to_sample(46), "oh")
        self.assertEqual(midi_to_sample(39), "cp")

    def test_name_to_sample(self):
        self.assertEqual(name_to_sample("Kick"), "bd")
        self.assertEqual(name_to_sample("Snare"), "sd")
        self.assertEqual(name_to_sample("Closed HiHat"), "hh")
        self.assertEqual(name_to_sample("Hand Clap"), "cp")

    def test_resolve_sample(self):
        self.assertEqual(resolve_sample(midi_note=36), "bd")
        self.assertEqual(resolve_sample(track_name="Kick"), "bd")
        self.assertEqual(resolve_sample(midi_note=38, track_name="Hats"), "sd")  # MIDI takes priority if valid


if __name__ == "__main__":
    unittest.main()
