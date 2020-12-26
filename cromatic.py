# -*- coding: utf-8 -*-

from PIL import Image
from helpers import diagonalize_array, verify_path
import os

# Returns a resized bar of longitude n x 1 from a chromatic bar file
def colorbar(image, longitude):
    return Image.open(image).resize((longitude, 1))

# Resize an image to 1x1
def pixel_resize(image):
    return Image.open(image).resize((1, 1))

# Creates a temporal directory in temp_db_dir with every image in path resized to 1 x 1
# Returns the number of images correctly resized and put into the temporary directory
def temp_img_dir(path, temp_dir=""):
    counter = 0
    temp_dir = verify_path(temp_dir)

    try:
        for image in os.listdir(path):
            if "mp4" in image:
                continue
            else:
                img = pixel_resize(path + image)
                img.save(f"{temp_dir}/{image}")
                counter += 1
        return counter
    except Exception as e:
        print(f"Error at {counter} photos. Cause: {e}")
        return counter


# Take as inputs a directory of album covers, a temp_dir, a chromatic bar image
# and the size of the final collage array. Returns an ordered list with the most
# similar albums according to the bar image.
def bar_mapping(directory, bar, size, temp_dir=""):
    temp_dir = verify_path(temp_dir)
    temp_img_dir(directory, temp_dir)
    mapping = []
    bar = colorbar(bar, size ** 2).convert('RGB')

    for i in range(0, size ** 2):
        rc, gc, bc = bar.getpixel((i, 0))
        mindif = 1000

        # For each color in the resized bar, loops through every album in the temp_dir
        # and appends to mapping list the filename of the cover with less color difference
        # that's not already in the list
        for image in os.listdir(temp_dir):
            folder = f"{temp_dir}/{image}"
            cover = Image.open(folder).convert('RGB')
            r, g, b = cover.getpixel((0, 0))
            diff = (((rc - r)**2) + ((gc - g)**2) + ((bc - b)**2))**0.5

            if diff < mindif and not image in mapping:
                mindif = diff
                cover_name = image
        mapping.append(cover_name)

    # Removes residual resources from the temporary directory
    for image in os.listdir(temp_dir):
        os.remove(f"{temp_dir}/{image}")
    return diagonalize_array(mapping)

# Returns an n x n collage according to a list of cover that contain the filenames of a 
# cover directory, from top to bottom, left to right. Saves in current directory
# Accepts a Python list of cover's filenames, its directory, and n (size). Name of the
# expected output and size per picture are given as optional parameters
def square_collage(cover_list, cover_dir, n, output="collage", spp = 100):
    collage = Image.new('RGB', (spp * n, spp * n))

    for i in range(0, len(cover_list)):
        img = Image.open(cover_dir + cover_list[i])
        width, height = img.size

        # Resizes the image maintaining aspect ratio
        if width > height:
            dif = (width - height) // 2
            box = (dif, 0, width - dif, height)
            img = img.crop(box)
        elif width < height:
            dif = (height - width) // 2
            box = (0, dif, width, height - dif)
            img = img.crop(box)

        img = img.resize((spp, spp))
        collage.paste(img, ((spp * i) % (spp * n), spp * ((spp * i) // (spp * n))))
    collage.save(f'{output}.png')
    print("Square collage done!")

    return True