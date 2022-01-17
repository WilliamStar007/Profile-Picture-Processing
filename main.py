# main.py
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import random

# open a target image
with Image.open(input("image name: ")) as im:
    # current image size
    x, y = im.size
    size = max(x, y)

    # a transparent mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + (size, size), fill=255)

    # generate grey background
    new_im = Image.new("RGB", (size//8, size//8))
    np_img = np.array(new_im)

    for r in range(0, size//8):
        for c in range(0, size//8):
            re = random.randint(60, 80) + random.randint(0, c//50) - random.randint(0, r//50) + random.randint(-3, 3)
            gr = random.randint(60, 80) + random.randint(0, c//50) - random.randint(0, r//50) + random.randint(-3, 3)
            bl = random.randint(60, 80) + random.randint(0, c//50) - random.randint(0, r//50) + random.randint(-3, 3)

            np_img[r][c] = [re, gr, bl]

    new_im = Image.fromarray(np_img, 'RGB')
    new_im = new_im.resize((size, size))

    # arr = np.random.randint(low=50, high=90, size=(size, size))
    # new_im = Image.fromarray(arr.astype('uint8'), 'L')
    # new_im = new_im.convert('RGB')
    # new_im = Image.new('RGB', (size, size), (105, 105, 105))

    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))

    output = ImageOps.fit(new_im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    output.save('output.png')
