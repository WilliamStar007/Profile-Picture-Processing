# circular.py
from PIL import Image, ImageOps, ImageDraw
import numpy as np

# open a target image
with Image.open(input("image name: ")) as im:
    # current image size
    size = (2048, 2048)

    # create mask
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    output = ImageOps.fit(im, mask.size, centering=(1.0, 0.15))
    output.putalpha(mask)

    output.save('result.png')
