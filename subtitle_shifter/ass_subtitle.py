import re
from datetime import timedelta
from .subtitle_shifter import SubtitleShifter

class ASSSubtitleShifter(SubtitleShifter):
    def parse_timecode(self, timecode):
        hours, minutes, seconds = timecode.split(':')
        seconds, milliseconds = seconds.split('.')
        return timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds), milliseconds=int(milliseconds) * 10)

    def format_timecode(self, td):
        total_seconds = int(td.total_seconds())
        milliseconds = td.microseconds // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:01}:{minutes:02}:{seconds:02}.{milliseconds // 10:02}"

    def shift_subtitles(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.startswith("Dialogue:"):
                    parts = line.split(',', 9)
                    start_time, end_time = self.shift_timecode(parts[1], parts[2])
                    parts[1] = start_time
                    parts[2] = end_time
                    outfile.write(','.join(parts) + '\n')
                else:
                    outfile.write(line)