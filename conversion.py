import os
from moviepy.editor import VideoFileClip

# Directory containing the downloaded videos
video_directory = 'downloaded_videos/'

# Directory to save the converted audio files
audio_directory = 'audio/'

# Ensure that the audio directory exists, if not create it
import os
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# List all files in the video directory
video_files = os.listdir(video_directory)

# Convert each video file to audio
for video_file in video_files:
    # Create the full path of the video file
    video_path = os.path.join(video_directory, video_file)
    
    # Create the full path of the audio file
    audio_file = os.path.splitext(video_file)[0] + '.mp3'
    audio_path = os.path.join(audio_directory, audio_file)

    try:
        # Load the video clip
        video_clip = VideoFileClip(video_path)
        
        # Extract audio from the video clip
        audio_clip = video_clip.audio
        
        # Write the audio clip to a file
        audio_clip.write_audiofile(audio_path, codec='mp3')
        
        # Close the video clip
        video_clip.close()
        
        print(f'Converted {video_file} to {audio_file}')
    except Exception as e:
        print(f'Error converting {video_file}: {e}')

print('All videos converted to audio successfully!')