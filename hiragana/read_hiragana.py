from Util import read_kana, data_definitions, encoding
import numpy
import os


def read_hiragana():
    metadata = data_definitions.hiragana_definition
    shokuon = ['ぅ', 'ぃ', 'ぇ', 'ぁ', 'っ', 'ゃ', 'ょ', 'ゅ', 'ゎ']
    bad_ten = []
    for letter in shokuon:
        bad_ten.append(encoding.char_to_kuten(letter)[1])
    hiragana = numpy.zeros([metadata.class_count, metadata.dataset_count, metadata.resolution[1], metadata.resolution[0]], dtype=numpy.uint8)
    for i in range(1, 33):
        file_name = 'ETL8G/ETL8G_{:02d}'.format(i)
        with open(file_name, 'rb') as f:
            for j in range(metadata.dataset_per_physical_file):
                count = 0
                for k in range(metadata.total_classes):
                    record = read_kana.read_next(f, metadata)
                    ku, ten = encoding.jis_0208_to_kuten(record[0])
                    if ku != 4 or ten in bad_ten:
                        continue
                    hiragana[count, metadata.dataset_per_physical_file * (i - 1) + j] = numpy.array(record[1])
                    count += 1
    numpy.savez_compressed(os.path.join(os.getcwd(), "hiragana", "data", "hiragana.npz"), hiragana)
