import re
from datetime import timedelta

def parse_timecode(timecode):
    hours, minutes, seconds, milliseconds = map(int, re.split('[:,]', timecode))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)

def format_timecode(td):
    total_seconds = int(td.total_seconds())
    milliseconds = td.microseconds // 1000
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def shift_timecode(line, delta):
    start, end = line.split(' --> ')
    start_td = max(parse_timecode(start) + delta, timedelta(0))
    end_td = max(parse_timecode(end) + delta, timedelta(0))
    return f"{format_timecode(start_td)} --> {format_timecode(end_td)}"

def sync_subtitles(input_file, output_file, delta_seconds):
    delta = timedelta(seconds=delta_seconds)
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if '-->' in line:
                outfile.write(shift_timecode(line.strip(), delta) + '\n')
            else:
                outfile.write(line)

if __name__ == "__main__":
    input_file = "A.Quiet.Place.Day.One.2024.2160p.WEB-DL.DDP5.1.Atmos.HDR.H265-Vietsub.srt"  # Replace with your input file name
    output_file = "A.Quiet.Place.Day.One.2024.2160p.WEB-DL.DDP5.1.Atmos.HDR.H265-Vietsub_synced.srt"  # Output file with postfix _synced
    delta_seconds = 6.5  # Replace with the number of seconds to add or subtract

    sync_subtitles(input_file, output_file, delta_seconds)
    print(f"Subtitles have been synced and saved to {output_file}")
