from scipy import misc
import colorsys
from __future__ import division
from optparse import OptionParser


# Set up input parameters
parser = OptionParser('usage: -f image.img -i .5')

parser.add_option("-f", dest="imagefile",
                  help="image file")
parser.add_option("-i", 
                  dest="intensity", default=.5,
                  help="The level of intensity [0,1] to flatten the image to.")

(options, args) = parser.parse_args()

# Read in image file
img = misc.imread(options.imagefile)

# For each pixel (top to bottom, left to right):
for x in [0:img.size[0]]
    for y in [0:img.size[1]]
        # Convert rgb to hls and modify the l attribute to
        # the intensity given by the user. Reconvert back to
        # rgb and write back to the image object on this pixel
        

# Save the modified image to a new file.



