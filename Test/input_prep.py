import numpy
import os
from hiragana import hiragana_classes
from katakana import katakana_classes
import sys
from PIL import Image

classes = hiragana_classes.hiragana_literals
# romanji_class_dict = hiragana_classes.romanji_to_class
romanji_class_dict = katakana_classes.romanji_to_class


def prepare_data(subdir, dimensions, channel):
    working_dir = os.getcwd()
    image_dir = os.path.join(working_dir, subdir)
    image_dir_list = os.listdir(image_dir)
    operating_system_delim = "\\" if sys.platform.startswith("win") else "/"

    height, width = dimensions
    images = []
    class_list = []

    for root, dirs, files in os.walk(image_dir):
        current_sub_directory = root.rsplit(operating_system_delim, 1)
        value = romanji_class_dict.get(current_sub_directory[1])
        if value is None:
            continue
        for file in files:
            class_list.append(value)
            with Image.open(os.path.join(root, file), 'r') as image:
                gray_scale = image.convert('L')
                gray_scale = gray_scale.resize((height, width))
                im_arr = numpy.asarray(gray_scale)
                images.append(numpy.asarray(gray_scale))

    class_array = numpy.array(class_list)
    class_array = numpy.reshape(class_array, (class_array.size, 1))
    # class_array = tensorflow.keras.utils.to_categorical(class_array, 71)
    images_array = numpy.zeros([len(image_dir_list), height, width], dtype=numpy.float32)
    images_array = numpy.asarray(images)
    images_array = images_array.reshape(len(images_array), height, width, channel)
    images_array = images_array/numpy.max(images_array)
    return images_array, class_array
