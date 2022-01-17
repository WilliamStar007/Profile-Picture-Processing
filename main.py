# main.py
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import random

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
    arr = np.random.randint(low=60, high=70, size=(size, size, 3))
    new_im = Image.fromarray(arr.astype('uint8'))
    # new_im = Image.new('RGB', (size, size), (100, 100, 100))

    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))

    output = ImageOps.fit(new_im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    output.save('output.png')
