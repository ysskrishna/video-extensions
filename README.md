# Video Extensions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ysskrishna/video-extensions/blob/main/LICENSE)
![Tests](https://github.com/ysskrishna/video-extensions/actions/workflows/test.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/video-extensions)](https://pypi.org/project/video-extensions/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/video-extensions?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/video-extensions)

Check if a file or extension is a video type, and iterate over 36 known video file formats. Python port of [video-extensions](https://github.com/sindresorhus/video-extensions) npm package.

## Features

- Immutable collection of 36 known video file extensions  
- Fast membership checks using `frozenset`  
- Case-insensitive and dot-aware checks  
- Works for both extensions and full file paths  
- Supports dotfiles (e.g., `.mov`)  
- Zero dependencies, minimal overhead  

## Installation

```bash
pip install video-extensions
```

Or using `uv`:

```bash
uv add video-extensions
```

## Usage

### Check if an extension is a video type

```python
from video_extensions import is_video_extension

is_video_extension("mp4")      # True
is_video_extension(".mov")     # True (dot-aware)
is_video_extension("AVI")      # True (case-insensitive)
is_video_extension("txt")      # False
```

### Check if a file path has a video extension

```python
from video_extensions import is_video_path

is_video_path("movie.mp4")                    # True
is_video_path("/path/to/video.MOV")           # True (case-insensitive)
is_video_path("presentation.avi")             # True
is_video_path("document.txt")                 # False
is_video_path(".mov")                         # True (dotfile support)
```

### Access the list of video extensions

```python
from video_extensions import VIDEO_EXTENSIONS, VIDEO_EXTENSIONS_LOWER

# VIDEO_EXTENSIONS is a frozenset of all known video extensions
print(len(VIDEO_EXTENSIONS))  # 36
"mp4" in VIDEO_EXTENSIONS     # True
"txt" in VIDEO_EXTENSIONS     # False

# VIDEO_EXTENSIONS_LOWER contains all extensions in lowercase
# Useful for case-insensitive lookups without calling .lower() repeatedly
"MP4" in VIDEO_EXTENSIONS_LOWER  # True (case-insensitive)

# Iterate over all extensions
for ext in sorted(VIDEO_EXTENSIONS):
    print(ext)
```

## Supported Extensions

The package includes support for 36 video file extensions:

- **Common formats**: mp4, mov, avi, mkv, webm, flv, wmv, mpg, mpeg
- **Streaming**: m3u8, m4v, m4p, ogv, ogg
- **Professional**: mxf, drc, aaf, roq
- **Legacy**: 3gp, 3g2, asf, vob, rm, rmvb, qt
- **Specialized**: avchd, m2v, mp2, mpe, mpv, mng, nsv, svi, yuv, wmv

## Credits

This package is a Python port of the [video-extensions](https://github.com/sindresorhus/video-extensions) npm package by [Sindre Sorhus](https://github.com/sindresorhus).


## Changelog

See [CHANGELOG.md](https://github.com/ysskrishna/video-extensions/blob/main/CHANGELOG.md) for a detailed list of changes and version history.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](https://github.com/ysskrishna/video-extensions/blob/main/CONTRIBUTING.md) for details on our code of conduct, development setup, and the process for submitting pull requests.


## Support

If you find this library useful, please consider:

- ⭐ **Starring** the repository on GitHub to help others discover it.
- 💖 **Sponsoring** to support ongoing maintenance and development.

[Become a Sponsor on GitHub](https://github.com/sponsors/ysskrishna) | [Support on Patreon](https://patreon.com/ysskrishna)

## License

MIT License - see [LICENSE](https://github.com/ysskrishna/video-extensions/blob/main/LICENSE) file for details.


## Author

**Y. Siva Sai Krishna**

- GitHub: [@ysskrishna](https://github.com/ysskrishna)
- LinkedIn: [ysskrishna](https://linkedin.com/in/ysskrishna)
