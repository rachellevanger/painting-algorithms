from __future__ import division

from scipy import misc
import convert_color_mode as ccm
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
for x in range(0,img.shape[0]):
    for y in range(0,img.shape[1]):
        # Convert rgb to hls and modify the l attribute to
        # the intensity given by the user. Reconvert back to
        # rgb and write back to the image object on this pixel
        
        rgb = img[x,y,:]/255

        hls = list(ccm.rgb_to_his(rgb[0],rgb[1],rgb[2]))

        his[1] = float(options.intensity)

        rgb = list(ccm.his_to_rgb(his[0],his[1],his[2]))

        rgb = [int(i*255) for i in rgb]

        img[x,y,:] = rgb


# Save the modified image to a new file.
misc.imsave('hoopoe_intensity_%s.jpg' % options.intensity, img)


