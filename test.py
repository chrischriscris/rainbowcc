# -*- coding: utf-8 -*-
from cromatic import  square_collage, bar_mapping
import os, sys

f = lambda path: int(len(os.listdir(path))**0.5)

user = sys.argv[1]

DIR = f'/home/leochris/Instagram/{user}/'
TEMP_DIR = '/home/leochris/Documentos/Programación/Python/collage/temp/'
BAR = '/home/leochris/Documentos/Programación/Python/collage/croma.jpeg'

size = f(DIR)

# Returns rainbow square collage, takes name of the output and 
# size of the collage
def main(n, output="collage", spp=100):
	cover_list = bar_mapping(DIR, TEMP_DIR, BAR, n)
	square_collage(cover_list, DIR, n, output, spp)

main(size, f'{user}_collage', 2000//size)