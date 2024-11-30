import unittest
from subtitle_shifter.srt_subtitle import SRTSubtitleShifter

class TestSRTSubtitleShifter(unittest.TestCase):
    def test_shift_timecode(self):
        shifter = SRTSubtitleShifter(6.5)
        start, end = shifter.shift_timecode("00:01:02,000", "00:01:04,000")
        self.assertEqual(start, "00:01:08,500")
        self.assertEqual(end, "00:01:10,500")

if __name__ == "__main__":
    unittest.main()