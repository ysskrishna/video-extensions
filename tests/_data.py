# Video extensions used for tests
VIDEO_EXAMPLES = ["mp4", "mov", "avi", "mkv", "webm", "flv", "wmv", "mpg", "mpeg"]
NON_VIDEO_EXAMPLES = ["txt", "md", "py", "js", "html", "css", "json", "xml"]

# Paths for testing is_video_path
VIDEO_PATHS = [
    "movie.mp4",
    "video.mov",
    "film.avi",
    "recording.mkv",
    "clip.webm",
    "stream.flv",
    "presentation.wmv",
]

NON_VIDEO_PATHS = [
    "readme.txt",
    "script.py",
    "style.css",
    "index.html",
    "data.json",
    "config.xml",
]

HIDDEN_VIDEO_PATHS = [".hidden.mp4", ".config.mov"]
HIDDEN_NON_VIDEO_PATHS = [".gitignore"]
