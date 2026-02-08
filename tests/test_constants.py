import pytest
from video_extensions import VIDEO_EXTENSIONS
from ._data import VIDEO_EXAMPLES


def test_video_extensions_type_and_content():
    """Check VIDEO_EXTENSIONS is a non-empty frozenset"""
    assert isinstance(VIDEO_EXTENSIONS, frozenset)
    assert len(VIDEO_EXTENSIONS) > 0


@pytest.mark.parametrize("ext", VIDEO_EXAMPLES)
def test_common_video_extensions_present(ext):
    """Check that common video extensions are present in VIDEO_EXTENSIONS"""
    assert ext in VIDEO_EXTENSIONS
