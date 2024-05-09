from moviepy.editor import AudioFileClip
import os

# Directory containing the audio files
audio_directory = 'audio/'

# Directory to save the extracted audio files
extracted_audio_directory = 'extracted_audio/'

# Ensure that the extracted audio directory exists, if not create it
if not os.path.exists(extracted_audio_directory):
    os.makedirs(extracted_audio_directory)

# List all files in the audio directory
audio_files = os.listdir(audio_directory)

# Extract the first 25 seconds from each audio file
for audio_file in audio_files:
    # Create the full path of the audio file
    audio_path = os.path.join(audio_directory, audio_file)
    
    # Create the full path of the extracted audio file
    extracted_audio_file = os.path.splitext(audio_file)[0] + '_extracted.mp3'
    extracted_audio_path = os.path.join(extracted_audio_directory, extracted_audio_file)

    try:
        # Load the audio clip
        audio_clip = AudioFileClip(audio_path)
        
        # Extract the first 25 seconds
        extracted_audio_clip = audio_clip.subclip(0, 25)
        
        # Write the extracted audio to a file
        extracted_audio_clip.write_audiofile(extracted_audio_path, codec='libmp3lame')
        
        print(f'Extracted first 25 seconds from {audio_file} and saved as {extracted_audio_file}')
    except Exception as e:
        print(f'Error extracting {audio_file}: {e}')

print('Extraction completed successfully!')
