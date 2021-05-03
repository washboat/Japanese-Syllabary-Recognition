import os
import numpy
from PIL import Image

dims = 64
image_array = numpy.zeros([1, dims, dims], dtype=numpy.float32)
image = Image.open(os.path.join(os.getcwd(), "../WrittenHiragana"))
