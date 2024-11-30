# Subtitle Shifter

This project provides tools to shift and convert subtitle files in `.srt` and `.ass` formats.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/subtitle-shifter.git
cd subtitle-shifter
pip install -r [requirements.txt](http://_vscodecontentref_/3)
```

## Features

- Shift subtitles in `.srt` format
- Shift subtitles in `.ass` format
- Convert `.ass` subtitles to `.srt` format

## Usage

### Shifting `.srt` Subtitles

```python
from subtitle_shifter.srt_subtitle import SRTSubtitleShifter

shifter = SRTSubtitleShifter(delta_seconds=6.5)
shifter.shift_subtitles("input.srt", "output_synced.srt")
```

### Shifting .ass Subtitles

```python
from subtitle_shifter.ass_subtitle import ASSSubtitleShifter

shifter = ASSSubtitleShifter(delta_seconds=2.5)
shifter.shift_subtitles("input.ass", "output_synced.ass")
```

### Converting .ass to .srt

```python
from subtitle_shifter.ass2srt import ASS2SRTConverter

converter = ASS2SRTConverter()
converter.convert("input.ass", "output.srt")
```