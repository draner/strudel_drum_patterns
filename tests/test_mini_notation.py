import unittest
from strudel_converter.mini_notation import optimize_track_pattern, optimize_beat_group


class TestMiniNotation(unittest.TestCase):
    def test_optimize_beat_group(self):
        self.assertEqual(optimize_beat_group("----", "hh"), "~")
        self.assertEqual(optimize_beat_group("xxxx", "hh"), "hh*4")
        self.assertEqual(optimize_beat_group("x---", "hh"), "[hh ~ ~ ~]")

    def test_optimize_track_pattern_shortcuts(self):
        self.assertEqual(optimize_track_pattern("x-x-x-x-x-x-x-x-", "hh"), "hh*8")
        self.assertEqual(optimize_track_pattern("x---x---x---x---", "bd"), "bd*4")
        self.assertEqual(optimize_track_pattern("----x-------x---", "sd"), "~ sd ~ sd")
        self.assertEqual(optimize_track_pattern("x-------x-------", "bd"), "bd ~ bd ~")


if __name__ == "__main__":
    unittest.main()
