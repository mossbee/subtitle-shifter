import re

def ass_to_srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        srt_index = 1
        for line in infile:
            if line.startswith("Dialogue:"):
                parts = line.split(",", 9)
                start_time = convert_time(parts[1])
                end_time = convert_time(parts[2])
                text = re.sub(r'{.*?}', '', parts[9]).replace("\\N", "\n").strip()
                outfile.write(f"{srt_index}\n{start_time} --> {end_time}\n{text}\n\n")
                srt_index += 1

def convert_time(ass_time):
    hours, minutes, seconds = ass_time.split(":")
    seconds, milliseconds = seconds.split(".")
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds)*10:03}"

if __name__ == "__main__":
    input_file = "Fly.Me.To.The.Moon.2024.ass"  # Replace with your input file name
    output_file = "Fly.Me.To.The.Moon.2024.srt"  # Output file name

    ass_to_srt(input_file, output_file)
    print(f"Subtitles have been converted and saved to {output_file}")
