import os.path
from video_extensions._data import VIDEO_EXTENSIONS

__all__ = ["VIDEO_EXTENSIONS", "is_video_extension", "is_video_path"]

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

def is_video_path(file_path: str) -> bool:
    """
    Return True if the file path has a video file extension.

    Examples:
        >>> is_video_path("movie.mp4")
        True
        >>> is_video_path("document.txt")
        False
        >>> is_video_path("/path/to/video.MOV")
        True
    """
    basename = os.path.basename(file_path)
    _, ext = os.path.splitext(file_path)
    
    # Handle dotfiles (files starting with a dot that have no extension)
    # e.g., .something where "something" is a video extension
    if not ext and basename.startswith(".") and len(basename) > 1:
        # Treat the entire filename (without leading dot) as the extension
        ext = basename[1:]
    else:
        ext = ext.lstrip(".")
    
    return ext.lower() in VIDEO_EXTENSIONS

