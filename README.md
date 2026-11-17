# Video Extensions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ysskrishna/video-extensions/blob/main/LICENSE)
[![Tests](https://github.com/ysskrishna/video-extensions/actions/workflows/test.yml/badge.svg)](https://github.com/ysskrishna/video-extensions/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/video-extensions)](https://pypi.org/project/video-extensions/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/video-extensions?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/video-extensions)
[![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)
[![Context7](https://img.shields.io/badge/Context7-docs-18181B)](https://context7.com/ysskrishna/video-extensions)
[![Ask DeepWiki](https://img.shields.io/badge/DeepWiki-ask-18181B)](https://deepwiki.com/ysskrishna/video-extensions)

Check if a file or extension is a video type, and iterate over 34 known video file formats including mp4, mov, avi, mkv, and more. Python port of [video-extensions](https://github.com/sindresorhus/video-extensions) npm package.

## Features

- Immutable collection of 34 known video file extensions  
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
print(len(VIDEO_EXTENSIONS))  # 34
"mp4" in VIDEO_EXTENSIONS     # True
"txt" in VIDEO_EXTENSIONS     # False

# VIDEO_EXTENSIONS_LOWER contains all extensions in lowercase
# Useful for case-insensitive lookups without calling .lower() repeatedly
"MP4" in VIDEO_EXTENSIONS_LOWER  # True (case-insensitive)

# Iterate over all extensions
for ext in sorted(VIDEO_EXTENSIONS):
    print(ext)
```

## API Reference

Install with `pip install video-extensions` and import from `video_extensions`. Signatures and descriptions below match the source code of `video_extensions`.

### `VIDEO_EXTENSIONS`

Constant: `frozenset` with 34 entries.

### `VIDEO_EXTENSIONS_LOWER`

Constant: `frozenset` with 34 entries.

### `is_video_extension(ext: str) -> bool`

Return True if the given file extension is known to be a video type.

**Example**

```python
from video_extensions import is_video_extension

is_video_extension("mp4")  # True
is_video_extension(".txt")  # False
```

### `is_video_path(file_path: str) -> bool`

Return True if the file path has a video file extension.

**Example**

```python
from video_extensions import is_video_path

is_video_path("movie.mp4")  # True
is_video_path("document.txt")  # False
is_video_path("/path/to/video.MOV")  # True
```

## Supported Extensions

The package includes support for 34 video file extensions:

- **Common formats**: mp4, mov, avi, mkv, webm, flv, wmv, mpg, mpeg
- **Streaming**: m3u8, m4v, m4p, ogv, ogg
- **Professional**: mxf, drc, aaf, roq
- **Legacy**: 3gp, 3g2, asf, vob, rm, rmvb, qt
- **Specialized**: avchd, m2v, mp2, mpe, mpv, mng, nsv, svi, yuv


## Contributing

Contributions are welcome! Please read our [Contributing Guide](https://github.com/ysskrishna/video-extensions/blob/main/CONTRIBUTING.md) for details on our code of conduct, development setup, and the process for submitting pull requests.


## Credits

This package is a Python port of the [video-extensions](https://github.com/sindresorhus/video-extensions) npm package by [Sindre Sorhus](https://github.com/sindresorhus).

## Built and maintained by

Video Extensions is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Changelog

See [CHANGELOG](CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/video-extensions/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://pypi.org/project/video-extensions/">Package on PyPI</a> •
  <a href="https://github.com/ysskrishna/video-extensions">GitHub Repository</a> •
  <a href="https://github.com/ysskrishna/video-extensions/releases">Release History</a> •
  <a href="https://github.com/ysskrishna/video-extensions/issues">Report Issues</a>
</p>
