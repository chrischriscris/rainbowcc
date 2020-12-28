# -*- coding: utf-8 -*-
import os
import shutil
from PIL import Image
from helpers import diagonalize_array, verify_path, colorbar, pixel_resize


class Collage:
    """ docstring for ClassName """
    def __init__(self, directory, color_coding, temp_directory="collage_temp"):
        self.directory = directory
        self.color_coding = color_coding
        counter = 0
        for a in os.listdir(directory):
            if a[-4:].lower() in [".jpg", ".png", ".jpeg"]:
                counter += 1
        self.temp_directory = temp_directory
        self.image_number = counter

    def __str__(self):
        return f"The collage will be made out of the images in {self.directory}, with {image_number} images.)"

    def make_collage(self, m, n, spp, output_name="collage"):
        ''' Returns an m x n collage according to the images of the instance
        directory. User chooses spp(size per picture) and (optional) output name
        '''

        # Makes a temporary directory which is mandatory to execute
        # the algorithm
        counter = 0
        verify_path(self.temp_directory)

        for image in os.listdir(self.directory):
            if image[-4:].lower() in [".jpg", ".png", ".jpeg"]:
                img = pixel_resize(f"{self.directory}/{image}")
                img.save(f"{self.temp_directory}/{image}")

        # Executes comparison algorithm according to the color_coding
        if m*n > self.image_number:
        	print(f"Not enough photos in the directory to make a {m}x{n} collage.")
        	return False
        mapping = []
        bar = colorbar(self.color_coding, m*n).convert('RGB')

        for i in range(0, m*n):
            rc, gc, bc = bar.getpixel((i, 0))
            mindif = 10**10
            photo_name = ""

            # For each color in the color_coding, loops through every image in the temp_directory
            # and appends to mapping list the filename of the image with less color difference
            # that's not already in the list 
            for image in os.listdir(self.temp_directory):
                image_route = f"{self.temp_directory}/{image}"
                post = Image.open(image_route).convert('RGB')
                r, g, b = post.getpixel((0, 0))
                diff = (((rc - r)**2) + ((gc - g)**2) + ((bc - b)**2))**0.5

                if diff < mindif and not image in mapping:
                    mindif = diff
                    photo_name = image
            mapping.append(photo_name)

        # Removes residual resources from the temporary directory
        shutil.rmtree(self.temp_directory)
        mapping = diagonalize_array(m, n, mapping)

        # Collage creation
        collage = Image.new('RGB', (spp * n, spp * m))

        for i in range(0, len(mapping)):

            img = Image.open(f'{self.directory}/{mapping[i]}')
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
        collage.save(f'{output_name}.png')
        print(f"{m}x{n} collage done!")
        return True

    def make_square_collage(self, spp, size=False, output_name="collage"):
        ''' Returns an n x n collage according to the images of the instance
        directory. User chooses spp(size per picture), size(optional, auto if not provided)
        and (optional) output name
        '''
        if not size:
            size = int(self.image_number ** 0.5)
        elif size**2 > self.image_number:
            print(f"Not enough photos in the directory to make a {size}x{size} collage.")
            return False

        self.make_collage(size, size, spp, output_name)
        return True