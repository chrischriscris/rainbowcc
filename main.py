# -*- coding: utf-8 -*-
# a command line tool made by chrischriscris

from cromatic import  square_collage, bar_mapping
import os, sys

f = lambda path: int(len(os.listdir(path))**0.5)

user = sys.argv[1]

DIR = f'/home/leochris/Instagram/{user}/'

if sys.argv[2] == '-r':
	BAR = 'rainbow.jpeg'
elif sys.argv[2] == '-l':
	BAR = 'luminosity.png'

size = f(DIR)

# Returns rainbow square collage, takes name of the output and 
# size of the collage
def main(n, output="collage", spp=100):
	cover_list = bar_mapping(DIR, BAR, n)
	square_collage(cover_list, DIR, n, output, spp)

main(size, f'{user}_collage_{sys.argv[2][-1]}', 2000//size)
