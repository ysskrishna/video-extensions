import pytest
from video_extensions import is_video_extension
from ._data import VIDEO_EXAMPLES, NON_VIDEO_EXAMPLES


@pytest.mark.parametrize("ext", VIDEO_EXAMPLES)
def test_video_extensions_true(ext):
    """Known video extensions should return True"""
    assert is_video_extension(ext)
    assert is_video_extension(f".{ext}")
    assert is_video_extension(ext.upper())
    assert is_video_extension(ext.title())


@pytest.mark.parametrize("ext", NON_VIDEO_EXAMPLES)
def test_non_video_extensions_false(ext):
    """Non-video extensions should return False"""
    assert not is_video_extension(ext)


@pytest.mark.parametrize("ext", ["", ".", "unknown", "xyz"])
def test_edge_cases_false(ext):
    """Edge cases should return False"""
    assert not is_video_extension(ext)
