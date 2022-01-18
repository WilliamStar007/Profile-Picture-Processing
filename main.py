# main.py
from PIL import Image, ImageOps, ImageDraw
import numpy as np

# open a target image
image_name = input("image name: ")
with Image.open(image_name) as im:
    # current image size
    x, y = im.size
    size = max(x, y)

    # create mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + (size, size), fill=255)

    # generate grey background
    np_data = np.array(im)
    back_grd_left = Image.fromarray(np_data[0:3543, 0:910])
    back_grd_right = Image.fromarray(np_data[0:3543, 2430:2835])
    grey_back_grd = Image.new('RGB', (size, size), (255, 255, 255))

    grey_back_grd.paste(back_grd_left, (0, 0))
    grey_back_grd.paste(back_grd_right, (2835, 0))
    grey_back_grd.paste(back_grd_right, (3240, 0))

    grey_back_grd.paste(im, (int((size - x) / 2), int((size - y) / 2)))

    output = ImageOps.fit(grey_back_grd, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    output.save('output.png')
