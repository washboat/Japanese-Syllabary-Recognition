from unittest import TestCase
from hiragana import hiragana_network, read_hiragana
from Util import split_kana, data_definitions
import custom_test
import os

class Test(TestCase):
    def test_hiragana_pipeline(self):
        dir = os.path.join(os.getcwd(), "hiragana", "data", "hiragana.npz")
        metadata = data_definitions.hiragana_definition
        output_resolution = 64

        read_hiragana.read_hiragana()
        split_kana.split(dir, metadata, output_resolution)
        hiragana_network.train_hiragana()
        custom_test.test_model(os.path.join("hiragana", "model", "hiragana.h5"), "WrittenHiragana", (64, 64), 1)



