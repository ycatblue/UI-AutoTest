# -*- coding: utf-8 -*-
import os
import time


def get_phone_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "files", "01400.jpg")
    return path


def download_file_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "files")
    return path


def get_screen_shot_path():
    file_name = "screenshot{}.png".format(time.strftime("%Y%m%d_%H%M%S"))
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "files", file_name)
    return path


if __name__ == '__main__':
    print(get_screen_shot_path())
