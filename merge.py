from pydub import AudioSegment
import os

# Directory containing the audio files to be merged
audio_directory = 'extracted_audio/'

# Ensure the directory exists
if not os.path.exists(audio_directory):
    print("Audio directory doesn't exist!")
    exit()

# List all audio files in the directory
audio_files = [file for file in os.listdir(audio_directory) if file.endswith('.mp3')]

# Ensure there are audio files to merge
if not audio_files:
    print("No audio files found in the directory!")
    exit()

# Initialize an empty audio segment for the final merged audio
merged_audio = AudioSegment.empty()

# Iterate through each audio file and append it to the merged audio segment
for audio_file in audio_files:
    # Load the audio file
    audio_path = os.path.join(audio_directory, audio_file)
    audio_segment = AudioSegment.from_file(audio_path)

    # Append the audio segment to the merged audio
    merged_audio += audio_segment

# Output file path for the merged audio
output_path = 'merged_audio.mp3'

# Export the merged audio to a single file
merged_audio.export(output_path, format='mp3')

print(f'Merged audio saved as {output_path}')
