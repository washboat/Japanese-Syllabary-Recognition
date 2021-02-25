from Util import read_kana as rk, data_definitions as dd, encoding
from hiragana import hiragana_classes as hc
import os
import struct
import numpy
from PIL import Image, ImageEnhance





def read_words():
    metadata = dd.kanji_definition
    x, y = metadata.resolution
    kanji = numpy.zeros([metadata.class_count, metadata.dataset_count, y, x], dtype=numpy.uint8)
    for i in range(1, 21):
        file_name = "ETL9G/ETL9G_{:02d}".format(i)
        with open(file_name, "rb") as file:
            for dataset_number in range(4):
                count = 0
                for j in range(3036):
                    record = rk.read_next(file, metadata)
                    ku, ten = encoding.jis_0208_to_kuten(record[1])
                    if ku < 16 or ku > 47:
                        continue
                    kanji[count, metadata.dataset_per_physical_file * (i - 1) + dataset_number] = numpy.array(record[-1])
                    count += 1
    numpy.savez_compressed(os.path.join(os.getcwd(), "kanji", "data", "kanji.npz"), kanji)


def test_read():
    metadata = dd.k9B_definition
    x, y = metadata.resolution
    kanji = numpy.zeros([metadata.class_count, metadata.dataset_count, y, x], dtype=numpy.uint8)
    for i in range(1, 5):
        file_name = "ETL9B/ETL9B_{:d}".format(i)
        with open(file_name, "rb") as file:
            for dataset_number in range(40):
                count = 0
                for j in range(3036):
                    record = rk.read_next(file, metadata)


