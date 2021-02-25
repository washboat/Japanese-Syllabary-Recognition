from Test import custom_test
from hiragana import read_hiragana, hiragana_network, convert_model
from katakana import read_katakana, katakana_network
from kanji import read_kanji, kanji_network
from Util import split_kana, data_definitions
import os


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# ToDo:
#   add dedicated tests
#   refactor EVERYTHING
#   buy a better computer so I can actually train a model on 2965 kanji
#   move kanji recognition to separate project
if __name__ == '__main__':
    # some quick and dirty testing
    read_hiragana.read_hiragana()
    split_kana.split(os.path.join(os.getcwd(), "hiragana", "data", "hiragana.npz"), data_definitions.hiragana_definition, 64)
    hiragana_network.train_hiragana()
    custom_test.test_model(os.path.join("hiragana", "model", "hiragana.h5"), "WrittenHiragana", (64, 64), 1)
    # convert_model.convert()
    #
    read_katakana.read()
    split_kana.split(os.path.join(os.getcwd(), "katakana", "data", "katakana.npz"), data_definitions.katakana_definition, 64)
    katakana_network.train_katakana()
    custom_test.test_model(os.path.join("katakana", "model", "katakana.h5"), "WrittenKatakana", (64, 64), 1)
    #
    read_kanji.read_words()
    split_kana.split_kanji(os.path.join(os.getcwd(), "kanji", "data", "kanji.npz"), data_definitions.kanji_definition, 64)
    kanji_network.train_kanji()
    #
    read_kanji.test_read()
    print_hi('PyCharm')

