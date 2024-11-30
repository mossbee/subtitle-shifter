import re
from datetime import timedelta

def parse_ass_timecode(timecode):
    hours, minutes, seconds = timecode.split(':')
    seconds, milliseconds = seconds.split('.')
    return timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds), milliseconds=int(milliseconds) * 10)

def format_ass_timecode(td):
    total_seconds = int(td.total_seconds())
    milliseconds = td.microseconds // 1000
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:01}:{minutes:02}:{seconds:02}.{milliseconds // 10:02}"

def shift_ass_timecode(line, delta):
    parts = line.split(',', 9)
    start_time = max(parse_ass_timecode(parts[1]) + delta, timedelta(0))
    end_time = max(parse_ass_timecode(parts[2]) + delta, timedelta(0))
    parts[1] = format_ass_timecode(start_time)
    parts[2] = format_ass_timecode(end_time)
    return ','.join(parts)

def sync_ass_subtitles(input_file, output_file, delta_seconds):
    delta = timedelta(seconds=delta_seconds)
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line.startswith("Dialogue:"):
                outfile.write(shift_ass_timecode(line.strip(), delta) + '\n')
            else:
                outfile.write(line)

if __name__ == "__main__":
    input_file = "Fly.Me.To.The.Moon.2024.ass"  # Replace with your input file name
    output_file = "Fly.Me.To.The.Moon.2024_synced.ass"  # Output file with postfix _synced
    delta_seconds = 2.5  # Replace with the number of seconds to add or subtract

    sync_ass_subtitles(input_file, output_file, delta_seconds)
    print(f"Subtitles have been synced and saved to {output_file}")
