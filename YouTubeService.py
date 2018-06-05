import os

import youtube_dl

youtube_options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'forcefilename': True,
    'outtmpl': 'data/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }]
}

video = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


class YouTubeService:
    def __init__(self):
        if not os.path.exists('data'):
            os.mkdir('data')

    def download(self, url):
        print("Init")
        with youtube_dl.YoutubeDL(youtube_options) as ydl:
            info_dict = ydl.extract_info(url, download=True)

            print("Ending dl")
