from katakana import katakana_classes as kc
from Util import read_kana, data_definitions, encoding
import os
import struct
import numpy as np


def read():
    metadata = data_definitions.katakana_definition
    katakana = np.zeros([metadata.class_count, metadata.dataset_count, metadata.resolution[1], metadata.resolution[0]], dtype=np.uint8)
    expected_duplicates_set = {"ｲ", "ｳ", "ｴ"}
    duplicate_counts = dict.fromkeys(expected_duplicates_set, 0)
    kana = kc.ETL1_katakana
    #  ETL dataset is not sorted. indices is a map of kana -> indices to aid in sorting data before writing to disk
    #  a non continuous set of values within indices indicate that there are duplicates
    indices = dict(zip(sorted(kana), range(len(kana))))
    char_index_limit = 8
    index = 0
    for i in range(7):
        # Only ETL1C files 07-13 have katakana data
        file_name = "ETL1/ETL1C_{:02d}".format(i + 7)
        with open(file_name, "rb") as file:
            if i == 6:
                # file ETL1C_13 only has 3 characters per sheet
                char_index_limit = 3
            for character_index in range(char_index_limit):
                for sheet_number in range(metadata.dataset_count):
                    try:  # kana ウ and ネ are missing one image, causing a struct error
                        r = read_kana.read_next(file, data_definitions.katakana_definition)
                    except struct.error as e:
                        print(e)
                        continue
                    if sheet_number == 0:
                        character = encoding.jis_0201_to_char(r[0])
                        if indices.get(character) is None:
                            continue
                        index = indices.get(character) - duplicate_counts.get(character, 0)
                        if character in expected_duplicates_set:
                            duplicate_counts[character] += 1
                    katakana[index, sheet_number] = np.array(r[1])
    path = os.path.join(os.getcwd(), "katakana", "data", "katakana.npz")
    np.savez_compressed(path, katakana)
