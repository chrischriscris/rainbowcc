# rainbowcc
Rainbow Collage Creator 

Create a beautiful square collage according to a color code.
(PIL required)

<h1>Usage</h1>
Download helpers.py and collageGen.py modules, and (optional) get rainbow.jpeg and luminosity.png

First import Collage class from collageGen into your python script.

<h2>Collage(directory, color_coding, temp_directory="collage_temp")</h2>
(paths can be absolute or relative)
<ul>
<li>directory is the path to a folder containing all the images (it will scan just .jpg and .png images)</li>
<li>color_coding is the path to an image of a color bar (see rainbow.jpeg)</li>
<li>temp_directory (optional) is the path to a temporary directory that will be created and the removed in order to execute the algorithm</li>
</ul>

<p>After you created an instace of Collage, use the <strong>make_square_collage(spp, output)</strong> method.</p>
<p>It'll take a mandatory parameter (spp), which is the size per picture of the collage, and output, which is the name of the result (it will be saved in the current directory as a png file).</p>

<h1>Example</h1>
<p>from collageGen import Collage</p>

<p>collage = Collage("my_img_dir", "rainbow.jpeg")</p>
<p>collage.make_square_collage(500, "beautifulCollage")</p>

<ul>

<li>The example will take any picture from "my_img_dir" directory and will output a square collage according to "rainbow.jpeg" in a filename called "beautifulCollage.png".</li>
<li>The size of every individual picture of the collage will be 500x500 (don't take care of aspect ratio, the algorithm crops the image before resizing it if it wasn't 1:1.</li>
<li>The size of the collage array is automatically decided by the method execution taking into account the square root of the number of images in the given directory.</li>
