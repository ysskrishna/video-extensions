import pytest
from video_extensions import is_video_path
from ._data import VIDEO_PATHS, NON_VIDEO_PATHS, HIDDEN_VIDEO_PATHS, HIDDEN_NON_VIDEO_PATHS


@pytest.mark.parametrize("path", VIDEO_PATHS + HIDDEN_VIDEO_PATHS)
def test_video_paths_true(path):
    """Paths with known video extensions should return True"""
    assert is_video_path(path)


@pytest.mark.parametrize("path", NON_VIDEO_PATHS + HIDDEN_NON_VIDEO_PATHS)
def test_non_video_paths_false(path):
    """Paths without known video extensions should return False"""
    assert not is_video_path(path)


@pytest.mark.parametrize("path", ["", ".", "..", "file", "path/to/file", "file.name.txt"])
def test_paths_without_extension_false(path):
    """Paths without extensions or with non-video extensions should return False"""
    assert not is_video_path(path)


@pytest.mark.parametrize(
    "path,expected",
    [
        ("file.backup.mp4", True),
        ("movie.old.avi", True),
        ("file.name.txt", False),
        ("C:\\Users\\file.mov", True),
        ("/path/to/document.txt", False),
        ("VIDEO.MP4", True),
        ("Movie.MOV", True),
        ("Film.AVI", True),
        ("file.TXT", False),
        ("/path/to/video.mp4", True),
        ("folder/subfolder/file.mkv", True),
        ("file.", False),
    ]
)
def test_paths_various(path, expected):
    """Edge cases: multiple dots, OS paths, case insensitivity, directories"""
    assert is_video_path(path) == expected
