import sys
import os
import random
import re
import requests 
import shutil
from pytube import YouTube
from pydub import AudioSegment
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch
import yt_dlp

def fetch_unique_video_urls(artist_name, num_videos):
    # Function to fetch unique video URLs related to the artist
    query = f"{artist_name} songs"
    search_url = f"https://www.youtube.com/results?search_query={query}"

    response = requests.get(search_url)
    html_content = response.text

    video_ids = re.findall(r'watch\?v=(\S{11})', html_content)

    if len(video_ids) < num_videos:
        print(f"Not enough videos found for {artist_name}.")
        sys.exit(1)

    unique_video_ids = random.sample(video_ids, num_videos)
    video_urls = [f"https://www.youtube.com/watch?v={vid}" for vid in unique_video_ids]

    return video_urls

def create_directory(directory):
    # Function to create a directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_videos(artist_name, num_videos):
    # Function to download videos related to the artist
    download_path = os.path.join(os.getcwd(), "downloads")
    create_directory(download_path)

    print(f"Downloading {num_videos} random videos of {artist_name} from YouTube...")

    downloaded_count = 0
    retry_limit = 2

    try:
        video_urls = fetch_unique_video_urls(artist_name, num_videos)

        for video_url in video_urls:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_path, f'video{downloaded_count + 1}.%(ext)s'),
                'max_duration': 250, 
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])

                downloaded_count += 1
                print(f"Downloaded video{downloaded_count}")

            except yt_dlp.DownloadError as e:
                print(f"Erro
