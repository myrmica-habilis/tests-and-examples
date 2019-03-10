# https://stackoverflow.com/questions/53673126

from PIL import BmpImagePlugin
import hashlib
from itertools import cycle

keys = hashlib.md5(b"aaaabbbb").digest()

input_image = BmpImagePlugin.BmpImageFile("img/tea.bmp")

# extract pure image data as bytes
image_data = input_image.tobytes()

# encrypt
image_data = bytes(a ^ b for a, b in zip(image_data, cycle(keys)))

# create new image, update with encrypted data and save
output_image = input_image.copy()
output_image.frombytes(image_data)
output_image.save("img/tea-encrypted.bmp")
