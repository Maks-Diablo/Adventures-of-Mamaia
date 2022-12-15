from moviepy.editor import VideoFileClip

import variables


def main():
    clip = VideoFileClip('assets/level1.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()
