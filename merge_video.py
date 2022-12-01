import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from loguru import logger

logger.add('logger.log', format='{time: YYYY-MM-DD at HH:mm:ss} | {level} | {message}', level='INFO', rotation='1 week',
           encoding='UTF-8')

@logger.catch()
def merge_videos():
    files = os.listdir(os.path.abspath('Videos'))
    path = os.path.abspath('Videos')

    all_uploaded_videos = []

    for file in files:
        all_uploaded_videos.append(VideoFileClip(os.path.join(path, file)).fx(vfx.fadein, 0.3).fx(vfx.fadeout, 0.3))

    logger.info('Starting to concatenate videos.')
    final_clip = concatenate_videoclips([video for video in all_uploaded_videos])

    logger.info('Starting to write file on the disk.')
    final_clip.write_videofile(os.path.join(path, '_Merged video.mp4'))
    logger.info('Video has been successfully merged!')


merge_videos()
