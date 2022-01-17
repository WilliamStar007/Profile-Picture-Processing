# main.py
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import random

# open a target image
with Image.open(input("image name: ")) as im:
    # current image size
    x, y = im.size
    size = max(x, y)

    # remove target image background
    np_data = np.array(im)

    for r in range(0, y):
        for c in range(0, x):
            if 30 < int(np_data[r][c][0]) < 100:
                if abs(int(np_data[r][c][0]) - int(np_data[r][c][1])) <= 10 and \
                   abs(int(np_data[r][c][0]) - int(np_data[r][c][2])) <= 10 and \
                   abs(int(np_data[r][c][1]) - int(np_data[r][c][2])) <= 10:
                    np_data[r][c][0], np_data[r][c][1], np_data[r][c][2] = 255, 255, 255

    im = Image.fromarray(np_data.astype('uint8'))

    # create mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + (size, size), fill=255)

    # generate grey background
    # arr = np.random.randint(low=60, high=80, size=(size, size))
    # new_im = Image.fromarray(arr.astype('uint8'), 'L')
    # new_im = new_im.convert('RGB')

    new_im = Image.new('RGB', (size, size), (255, 255, 255))
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))

    output = ImageOps.fit(new_im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    output.save('output.png')
