import os
from moviepy.editor import VideoFileClip, AudioFileClip
import re

# Folder paths
video_folder = 'videos'
audio_folder = 'audios'
output_folder = 'matched_videos'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Natural sort helper function
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# Main function to process all videos
def process_videos():
    # Get list of video and audio files and sort them naturally
    video_files = sorted([f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mov'))], key=natural_sort_key)
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith(('.mp3', '.wav'))], key=natural_sort_key)

    # Ensure that the number of videos matches the number of audio files
    for i in range(min(len(video_files), len(audio_files))):
        video_file = video_files[i]
        audio_file = audio_files[i]

        video_path = os.path.join(video_folder, video_file)
        audio_path = os.path.join(audio_folder, audio_file)

        print(f"Matching video: {video_file} with audio: {audio_file}")

        try:
            # Load video and audio
            video = VideoFileClip(video_path)
            audio = AudioFileClip(audio_path)

            # Set audio to video
            video_with_audio = video.set_audio(audio)

            # Output file path
            output_path = os.path.join(output_folder, f'matched_{video_file}')
            video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

            # Close the clips to free resources
            video.close()
            audio.close()
            video_with_audio.close()

        except Exception as e:
            print(f"Error processing {video_file} with {audio_file}: {e}")

if __name__ == '__main__':
    process_videos()
