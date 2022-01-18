# main.py
from PIL import Image, ImageOps, ImageDraw
import numpy as np

# open a target image
with Image.open(input("image name: ")) as im:
    # current image size
    x, y = im.size
    size = max(x, y)

    # create mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + (size, size), fill=255)

    # generate grey background
    np_data = np.array(im)
    left = Image.fromarray(np_data[0:y, 0:450])
    right = Image.fromarray(np_data[0:y, x-400:x])
    background = Image.new('RGB', (size, size))

    # piece together parts of the image
    background.paste(left, (0, 0))
    background.paste(right, (x+250, 0))
    background.paste(right, (3235, 0))
    background.paste(im, (int((size - x) / 2), int((size - y) / 2)))

    # fit the image for mask
    output = ImageOps.fit(background, mask.size, centering=(0.5, 0.5))

    # apply the mask
    output.putalpha(mask)
    output = output.resize((1181, 1181))

    output.save('output.png')
