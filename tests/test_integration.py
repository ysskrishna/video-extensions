import pytest
from video_extensions import VIDEO_EXTENSIONS, is_video_extension, is_video_path
from ._data import VIDEO_EXAMPLES, VIDEO_PATHS


@pytest.mark.parametrize("ext,path,expected", [
    ("mp4", "file.mp4", True),
    ("mov", "video.mov", True),
    ("txt", "readme.txt", False),
    ("avi", "movie.avi", True),
    ("py", "script.py", False),
])
def test_consistency_between_functions(ext, path, expected):
    """Both functions return consistent results"""
    assert is_video_extension(ext) == expected
    assert is_video_path(path) == expected


def test_all_extensions_in_set():
    """Ensure all extensions in VIDEO_EXTENSIONS are recognized"""
    for ext in VIDEO_EXTENSIONS:
        assert is_video_extension(ext) is True
        assert is_video_path(f"file.{ext}") is True
