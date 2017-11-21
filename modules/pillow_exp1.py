#!/usr/bin/python3

from PIL import Image

im = Image.open('1.jpg')

w, h = im.size
print('original image size: %s x %s' % (w, h))

im.thumbnail((w//2, h//2))
print('Resize image to: %s x %s' % (w//2, h//2))

im.save('test.jpg', 'jpeg')