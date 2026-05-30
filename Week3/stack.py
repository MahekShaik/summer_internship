import os

os.system(
    'ffmpeg -i videos/raw_r.mp4 '
    '-i videos/detect_r.mp4 '
    '-i videos/segment_r.mp4 '
    '-filter_complex "vstack=inputs=3" '
    'output/final_stacked.mp4'
)