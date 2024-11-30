import unittest
from subtitle_shifter.ass_subtitle import ASSSubtitleShifter

class TestASSSubtitleShifter(unittest.TestCase):
    def test_shift_timecode(self):
        shifter = ASSSubtitleShifter(2.5)
        start, end = shifter.shift_timecode("0:01:02.00", "0:01:04.00")
        self.assertEqual(start, "0:01:04.50")
        self.assertEqual(end, "0:01:06.50")

if __name__ == "__main__":
    unittest.main()