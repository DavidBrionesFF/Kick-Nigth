import os

DIRECTORIES = [
    "data/notes/"
]

def init_directories():
    for directory in DIRECTORIES:
        if not os.path.isdir(directory):
            os.mkdir(directory)