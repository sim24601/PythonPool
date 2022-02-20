#!/usr/bin/env python3

import os
from PIL import Image

path = "./supplier-data/images/"
target_directory = "./supplier-data/images/"


def main():
    for infile in os.scandir(path):
        if infile.is_file():
            outfile = os.path.join(target_directory, infile.name)
            try:
                with Image.open(infile.path) as img:
                    img.convert('RGB').resize((600, 400)).save(
                        outfile+".jpeg", "JPEG")
            except OSError as err:
                print(err)
    del infile, outfile


if __name__ == "__main__":
    main()
