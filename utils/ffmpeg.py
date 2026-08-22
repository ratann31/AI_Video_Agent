"""Locate FFmpeg before importing libraries that depend on it."""

import os
import shutil
from pathlib import Path


def configure_ffmpeg() -> str | None:
    """Add a known FFmpeg installation directory to this process's PATH."""
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg

    candidates = [
        Path(r"C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"),
        Path(r"C:\\ffmpeg\\bin\\ffmpeg.exe"),
    ]

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        winget_packages = Path(local_app_data) / "Microsoft" / "WinGet" / "Packages"
        candidates.extend(winget_packages.glob("Gyan.FFmpeg_*/ffmpeg-*/bin/ffmpeg.exe"))

    for candidate in candidates:
        if candidate.is_file():
            os.environ["PATH"] = f"{candidate.parent}{os.pathsep}{os.environ.get('PATH', '')}"
            return str(candidate)

    return None
