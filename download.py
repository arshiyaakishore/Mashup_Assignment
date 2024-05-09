from pytube import YouTube

# List of YouTube video URLs of Arijit Singh songs
video_urls = [
    'https://youtu.be/HrnrqYxYrbk?feature=shared',
    'https://youtu.be/KUpwupYj_tY?feature=shared',
    'https://youtu.be/EdftT8GMU1U?feature=shared',
    'https://youtu.be/BddP6PYo2gs?feature=shared',
    'https://youtu.be/FxAG_11PzCk?feature=shared',
    'https://youtu.be/Ov0YGGSY6gY?feature=shared',
    'https://youtu.be/_iktURk0X-A?feature=shared',
    'https://youtu.be/zXLgYBSdv74?feature=shared',
    'https://youtu.be/VOLKJJvfAbg?feature=shared',
    'https://youtu.be/hoNb6HuNmU0?feature=shared',
    'https://youtu.be/FJ55SHCzt88?feature=shared'
    # Example video URL
    # Add more URLs here for other videos
]

# Directory to save the downloaded videos
save_path = 'downloaded_videos/'

# Download each video
for i, url in enumerate(video_urls, 1):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(f'Downloading video {i}/{len(video_urls)}: {yt.title}...')
        video.download(save_path)
        print('Download completed!')
    except Exception as e:
        print(f'Error downloading video {i}: {e}')

print('All videos downloaded successfully!')
