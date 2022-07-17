import os
import uuid
import time
import random
from wrappers.pixabay_wrapper import search_high_quality_videos
from moviepy.editor import VideoFileClip, concatenate_videoclips
from engine.utils import delete_temp_dir, download_file_to_temp_dir, create_temp_dir, delete_temp_dir

def get_random_video(query):
    results = search_high_quality_videos(query)
    return random.choice(results)

def bake_timeline(timeline, output_path):
    process_name = "bake-timeline-" + str(uuid.uuid4()) 

    # Downloading all the clips to temp
    create_temp_dir(process_name)
    uuid_clips_sequence = []
    for i, clip_url in enumerate(timeline):
        clip_name = f"clip_{i}.mp4"
        clip_path = os.path.join("temp", process_name, clip_name)
        download_file_to_temp_dir(clip_url, process_name, clip_name)
        uuid_clips_sequence.append(clip_path)
    time.sleep(1)
    
    # Concatenating video clips
    video_clip_sequence = [ VideoFileClip(clip_path) for clip_path in uuid_clips_sequence ]
    final_clip = concatenate_videoclips(video_clip_sequence)
    final_clip.write_videofile(output_path)

    # Deleting temp dir
    delete_temp_dir(process_name)
    
def create_random_video_timeline(query, total_random_videos, output_path):
    clips = [ get_random_video(query)["url"] for _ in range(total_random_videos) ]
    bake_timeline(clips, output_path)

