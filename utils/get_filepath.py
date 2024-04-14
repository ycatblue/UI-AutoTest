# -*- coding: utf-8 -*-
import os


def get_phone_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "files", "01400.jpg")
    return path


if __name__ == '__main__':
    print(get_phone_path())