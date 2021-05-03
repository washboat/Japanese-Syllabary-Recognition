import os
from Test import custom_test
from Util import data_definitions, split_kana
from hiragana import hiragana_network, read_hiragana
from kanji import kanji_network, read_kanji
from katakana import katakana_network, read_katakana


def run_hira():
    read_hiragana.read_hiragana()
    split_kana.split(os.path.join(os.getcwd(), "hiragana", "data", "hiragana.npz"), data_definitions.hiragana_definition, 64)
    hiragana_network.train_hiragana()
    custom_test.test_model(os.path.join("hiragana", "model", "hiragana.h5"), "WrittenHiragana", (64, 64), 1)


def run_kata():
    # read_katakana.read()
    # split_kana.split(os.path.join(os.getcwd(), "katakana", "data", "katakana.npz"), data_definitions.katakana_definition, 64)
    # katakana_network.train_katakana()
    custom_test.test_model(os.path.join("katakana", "model", "katakana.h5"), "WrittenKatakana", (64, 64), 1)

def run_kanji():
    read_kanji.read_words()
    split_kana.split_kanji(os.path.join(os.getcwd(), "kanji", "data", "kanji.npz"), data_definitions.kanji_definition, 64)
    kanji_network.train_kanji()
    # read_kanji.test_read()


# ToDo:
#   add dedicated tests
#   refactor EVERYTHING
#   buy a better computer so I can actually train a model on 2965 kanji
#   move kanji recognition to separate project
if __name__ == '__main__':
    # Uncomment before run
    run_hira()
    run_kata()
    # run_kanji()

