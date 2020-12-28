# rainbowcc
_Rainbow Collage Creator_

_Create a beautiful square collage according to a color code._
_(PIL required)_

## Usage
Download helpers.py and rainbow.py modules, and (optional) get rainbow.jpeg and luminosity.png

First import Collage class from collageGen into your python script.

### Collage(directory, color_coding, temp_directory="collage_temp")
_(paths can be absolute or relative)_

+ directory is the path to a folder containing all the images (it will scan just .jpg and .png images)
+ color_coding is the path to an image of a color bar (see rainbow.jpeg)
+ temp_directory (optional) is the path to a temporary directory that will be created and the removed in order to execute the algorithm


After you created an instace of Collage, use the <strong>make_square_collage(spp, size, output)</strong> method.
It'll take a mandatory parameter (spp), which is the size per picture of the collage, and tow optional parameters: size (which is auto by default), and output, which is the name of the result (it will be saved in the current directory as a png file).

#### Example

  from collageGen import Collage

  collage = Collage("my_img_dir", "rainbow.jpeg")
  collage.make_square_collage(500, "beautifulCollage")

+ The example will take any picture from "my_img_dir" directory and will output a square collage according to "rainbow.jpeg" in a filename called "beautifulCollage.png".
+ The size of every individual picture of the collage will be 500x500 (don't take care of aspect ratio, the algorithm crops the image before resizing it if it wasn't 1:1.
+ The size of the collage array (if not provided) is automatically decided by the method execution taking into account the square root of the number of images in the given directory.
