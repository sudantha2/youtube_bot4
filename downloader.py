import yt_dlp
import os

def download_video(url, quality="360p", audio_only=False):
    # Ensure downloads directory exists
    os.makedirs("downloads", exist_ok=True)

    # Choose format based on audio or video
    format_string = "bestaudio" if audio_only else f"bestvideo[height<={quality[:-1]}]+bestaudio/best"

    ydl_opts = {
        "format": format_string,
        "outtmpl": "downloads/%(title).50s.%(ext)s",
        "merge_output_format": "mp4",
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
        # If MP3 requested, change extension manually (yt-dlp won't always rename it)
        if audio_only:
            base, _ = os.path.splitext(file_path)
            return base + ".mp3" if os.path.exists(base + ".mp3") else file_path
        return file_path
