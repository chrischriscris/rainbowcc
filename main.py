# -*- coding: utf-8 -*-
# a command line tool made by chrischriscris

from cromatic import  square_collage, bar_mapping
from subprocess import call
import os, sys, shutil

f = lambda path: int(len(os.listdir(path))**0.5)
user = sys.argv[1]
call(f'instagram-scraper {user}', shell=True)
DIR = f'{user}'

if sys.argv[2] == '-r':
	BAR = 'rainbow.jpeg'
elif sys.argv[2] == '-l':
	BAR = 'luminosity.png'

size = f(DIR)

def main(n, DIR, BAR, output="collage", spp=100):
	cover_list = bar_mapping(DIR, BAR, n)
	square_collage(cover_list, DIR, n, output, spp)
	shutil.rmtree(DIR)

main(size, DIR, BAR, f'{user}_collage_{sys.argv[2][-1]}', 2000//size)

