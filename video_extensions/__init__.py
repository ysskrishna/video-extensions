from video_extensions._data import VIDEO_EXTENSIONS

__all__ = ["VIDEO_EXTENSIONS", "is_video_extension"]

def is_video_extension(ext: str) -> bool:
    """
    Return True if the given file extension is known to be a video type.

    Examples:
        >>> is_video_extension("mp4")
        True
        >>> is_video_extension(".txt")
        False
    """
    return ext.lower().lstrip(".") in VIDEO_EXTENSIONS
