#!/usr/bin/env python3

import ctypes
import os
import sys
from time import sleep


def main():
    # get user defined background folder
    # if len(sys.argv) != 2:
    #     print("Please provide the folder where your pictures are located")
    #     path = input("Folder: ")
    # else:
    #     path = sys.argv[1]

    # since this is personal, just hard coding path
    path = "C:\\Users\\Backal\\Backgrounds"
    while True:
        backgrounds = get_picture_list(path)
        if len(backgrounds) == 0:
            print("No pictures found in folder")
            return 1
        for i in backgrounds:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       os.path.join(path, i),
                                                       0)
            sleep(6)

    return 0


def get_picture_list(path):
    backgrounds = []
    for root, dirname, files in os.walk(path):
        backgrounds = [file for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]
    return backgrounds


if __name__ == "__main__":
    main()

