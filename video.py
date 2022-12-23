from moviepy.editor import VideoFileClip

import variables


def level_1_credits():
    clip = VideoFileClip('assets/video/credits_level_1.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_1_cut_scene():
    clip = VideoFileClip('assets/video/cut-scene-level1_1(0).mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_2_credits():
    clip = VideoFileClip('assets/video/credits_level_2.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_2_cut_scene():
    clip = VideoFileClip('assets/video/cut-scene-level2(0).mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_3_credits():
    clip = VideoFileClip('assets/video/credits_level_3.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_3_cut_scene():
    clip = VideoFileClip('assets/video/cut-scene-level3.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_4_credits():
    clip = VideoFileClip('assets/video/credits_level_4.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_4_cut_scene():
    clip = VideoFileClip('assets/video/cut-scene-level4(0).mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def level_final_credits():
    clip = VideoFileClip('assets/video/credits_end.mp4')
    clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
    clipresized.preview()


def the_end():
    clip2 = VideoFileClip('assets/video/the_end.mp4')
    clipresized2 = clip2.resize(height=variables.SCREEN_HEIGHT)
    clipresized2.preview()
