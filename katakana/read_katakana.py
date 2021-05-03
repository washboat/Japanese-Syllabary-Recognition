from katakana import katakana_classes as kc
from Util import read_kana, data_definitions, encoding
import os
import struct
import numpy as np

#
# reads ETL1 dataset and writes relevant data to npz file
# Uses JIS_X_0201 codes provided in dataset to determine what data is relevant
# JIS_X_0201 to UTF-8 conversions can be found in ../Util/encoding.py
#
def read():
    metadata = data_definitions.katakana_definition
    katakana = np.zeros([metadata.class_count, metadata.dataset_count, metadata.resolution[1], metadata.resolution[0]], dtype=np.uint8)
    # dataset has three duplicates
    expected_duplicates_set = {"ｲ", "ｳ", "ｴ"}
    duplicate_counts = dict.fromkeys(expected_duplicates_set, 0)
    kana = kc.ETL1_katakana

    # ETL dataset is not sorted, so I create a presorted map 'indices'.
    # the map is of kana -> indices. As kana is read, its data is placed into its predetermined index of the map
    # a non-continuous set of values inside 'indices' indicates that there are duplicates present.
    indices = dict(zip(sorted(kana), range(len(kana))))
    char_index_limit = 8
    index = 0
    for i in range(7):  # for every file in folder
        # Only ETL1C files 07-13 have katakana data
        file_name = "datasets/ETL1/ETL1C_{:02d}".format(i + 7)
        with open(file_name, "rb") as file:
            if i == 6:
                # file ETL1C_13 only has 3 characters per sheet
                char_index_limit = 3
            for character_index in range(char_index_limit):  # for character in file
                for sheet_number in range(metadata.dataset_count):  # for sheet in dataset
                    try:  # kana ウ and ネ are missing one image, causing a struct error
                        record = read_kana.read_next(file, data_definitions.katakana_definition)
                    except struct.error as e:
                        print(e)
                        continue
                    if sheet_number == 0:  # if start of new character data
                        character = encoding.jis_0201_to_char(record[0])
                        if indices.get(character) is None:  # if character is not katakana
                            continue
                        index = indices.get(character) - duplicate_counts.get(character, 0)
                        if character in expected_duplicates_set:
                            duplicate_counts[character] += 1
                    katakana[index, sheet_number] = np.array(record[1])
    path = os.path.join(os.getcwd(), "katakana", "data", "katakana.npz")
    np.savez_compressed(path, katakana)
