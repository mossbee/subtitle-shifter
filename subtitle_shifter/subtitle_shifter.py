from datetime import timedelta

class SubtitleShifter:
    def __init__(self, delta_seconds):
        self.delta = timedelta(seconds=delta_seconds)

    def shift_timecode(self, start, end):
        start_td = max(self.parse_timecode(start) + self.delta, timedelta(0))
        end_td = max(self.parse_timecode(end) + self.delta, timedelta(0))
        return self.format_timecode(start_td), self.format_timecode(end_td)

    def parse_timecode(self, timecode):
        raise NotImplementedError

    def format_timecode(self, td):
        raise NotImplementedError

    def shift_subtitles(self, input_file, output_file):
        raise NotImplementedError