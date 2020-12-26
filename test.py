# -*- coding: utf-8 -*-
from cromatic import  square_collage, bar_mapping

DIR = '/home/leochris/Instagram/chrischriscris/'
TEMP_DIR = '/home/leochris/Documentos/Programación/Python/collage/temp/'
BAR = '/home/leochris/Documentos/Programación/Python/collage/croma.jpeg'

# Returns rainbow square collage, takes name of the output and 
# size of the collage
def main(n, output="collage", spp=100):
	cover_list = bar_mapping(DIR, TEMP_DIR, BAR, n)
	square_collage(cover_list, DIR, n, output, spp)

main(7, "chus", 285)