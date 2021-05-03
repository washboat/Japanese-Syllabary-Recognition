from Util import read_kana, data_definitions, encoding
import numpy
import os

##
# reads ETL8G dataset and writes relevant data to npz file
# uses JIS_X_0208 codes provided in dataset to determine what data is relevant
# read more about JIS_X_0208: https://en.wikipedia.org/wiki/JIS_X_0208
# JIS_X_0208/kuten code table: http://www.asahi-net.or.jp/~AX2S-KMTN/ref/jisx0208.html
# kuten refers to the row and column the hiragana character resides in inside the code table
# ku = row, ten = column
# for hiragana, ku will always = 4
#
# JIS_X_0208 to UTF-8 conversions can be found in ../Util/encoding.py
#

def read_hiragana():
    metadata = data_definitions.hiragana_definition
    # small, or "half height", hiragana that we're not interested in
    little_hiragana = ['ぅ', 'ぃ', 'ぇ', 'ぁ', 'っ', 'ゃ', 'ょ', 'ゅ', 'ゎ']
    bad_ten = []
    # get kuten code for each character we're not interested in so we can skip them later
    for letter in little_hiragana:
        bad_ten.append(encoding.char_to_kuten(letter)[1])
    hiragana = numpy.zeros([metadata.class_count, metadata.dataset_count, metadata.resolution[1], metadata.resolution[0]], dtype=numpy.uint8)
    for i in range(1, 33):  # for each file in folder
        file_name = 'datasets/ETL8G/ETL8G_{:02d}'.format(i)
        with open(file_name, 'rb') as f:
            for j in range(metadata.dataset_per_physical_file):  # for each set of date per file
                count = 0
                for k in range(metadata.total_classes):  # for each category in the dataset
                    record = read_kana.read_next(f, metadata)
                    ku, ten = encoding.jis_0208_to_kuten(record[0])
                    if ku != 4 or ten in bad_ten:  # if not hiragana or not one of the hiragana we're interested in
                        continue
                    hiragana[count, metadata.dataset_per_physical_file * (i - 1) + j] = numpy.array(record[1])
                    count += 1
    numpy.savez_compressed(os.path.join(os.getcwd(), "hiragana", "data", "hiragana.npz"), hiragana)
