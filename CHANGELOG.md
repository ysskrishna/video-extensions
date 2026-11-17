# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-11-18

### Changed
- Package behavior is unchanged. This release publishes the same library through separate build, PyPI publish, and GitHub release steps.

## [1.0.0]

### Added
- Initial release of video-extensions Python package
- `is_video_extension()` function to check if a file extension is a video type
- `is_video_path()` function to check if a file path has a video extension
- `VIDEO_EXTENSIONS` frozenset containing 36 known video file extensions
- `VIDEO_EXTENSIONS_LOWER` constant containing all video extensions in lowercase for optimized case-insensitive lookups
- Support for case-insensitive extension checks
- Dot-aware extension handling (supports both "mp4" and ".mp4" formats)
- Dotfile support in `is_video_path()` function - now handles files like `.mov` where the entire filename (without leading dot) is treated as the extension
- Comprehensive test suite with unit and integration tests
- Type hints for better IDE support and type checking
- Zero dependencies for minimal overhead

### Features
- Immutable collection of 36 known video file extensions
- Fast membership checks using `frozenset`
- Support for common formats (mp4, mov, avi, mkv, webm), streaming formats (m3u8, m4v), professional formats (mxf, aaf), and more
- Python 3.8+ compatibility

[1.0.1]: https://github.com/ysskrishna/video-extensions/releases/tag/v1.0.1
[1.0.0]: https://github.com/ysskrishna/video-extensions/releases/tag/v1.0.0
