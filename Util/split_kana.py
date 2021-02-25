from sklearn.model_selection import train_test_split
import numpy
import os
import skimage.transform as skitr
from Util.data_definitions import katakana_definition, hiragana_definition


def split(data_path, metadata, output_resolution):
    class_count = metadata.class_count
    instance_count = metadata.dataset_count
    n = class_count * instance_count
    directory = os.path.dirname(data_path)
    x, y = metadata.resolution
    training_images = numpy.zeros([n, output_resolution, output_resolution], dtype=numpy.float32)
    kana = numpy.load(data_path)["arr_0"].reshape([-1, y, x]).astype(numpy.float32)
    num = numpy.max(kana)
    kana = kana / numpy.max(kana)

    for i in range(n):
        training_images[i] = skitr.resize(kana[i], (output_resolution, output_resolution))
    training_labels = None
    # classes = 0
    if metadata.name == "hiragana":
        classes = numpy.arange(metadata.class_count)
        training_labels = numpy.repeat(classes, metadata.dataset_count)
    elif metadata.name == "katakana":
        classes = numpy.arange(metadata.class_count - 3)
        duplicates = numpy.array([2, 3, 4])
        classes = numpy.append(duplicates, classes)
        classes = numpy.sort(classes)
        training_labels = numpy.repeat(classes, metadata.dataset_count)

        delete = []
        for i in range(len(training_images)):
            if (training_images[i] == numpy.zeros([training_images[i].shape[0], training_images[i].shape[1]],
                                                  dtype=numpy.uint8)).all():
                delete.append(i)
        training_images = numpy.delete(training_images, delete[0], axis=0)
        training_labels = numpy.delete(training_labels, delete[0])

        # training_images = numpy.delete(training_images, delete[1] - 1, axis=0)
        # training_labels = numpy.delete(training_labels, delete[1] - 1)

    training_images, testing_images, training_labels, testing_labels = train_test_split(training_images,
                                                                                        training_labels,
                                                                                        test_size=0.2)
    storage_path = os.path.join(directory, metadata.name)
    numpy.savez_compressed(storage_path + "_train_images.npz", training_images)
    numpy.savez_compressed(storage_path + "_train_labels.npz", training_labels)
    numpy.savez_compressed(storage_path + "_test_images.npz", testing_images)
    numpy.savez_compressed(storage_path + "_test_labels.npz", testing_labels)


def split_kanji(data_path, ct, output_resolution):
    class_count = ct.class_count
    instance_count = ct.dataset_count
    n = class_count * instance_count
    directory = os.path.dirname(data_path)
    x, y = ct.resolution
    training_images = numpy.zeros([n, output_resolution, output_resolution], dtype=numpy.float32)
    kanji = numpy.load(data_path)["arr_0"].reshape([-1, y, x]).astype(numpy.float32)
    # kanji = numpy.memmap(data_path, mode="r", dtype=numpy.float32, shape=(n, y, x))["arr_0"]
    print(numpy.max(kanji))
    # kanji = kanji / numpy.max(kanji)
    # normalize = lambda p, q: p / q
    # normalized_kanji = kanji
    # normalized_kanji = normalize(kanji, numpy.max(kanji))
    # normalized_kanji = kanji / numpy.max(kanji)
    print("kanji normalized")
    for i in range(n):
        training_images[i] = skitr.resize(kanji[i], (output_resolution, output_resolution))

    print("images created")
    classes = numpy.arange(ct.class_count)
    training_labels = numpy.repeat(classes, ct.dataset_count)

    training_images, testing_images, training_labels, testing_labels = train_test_split(training_images,
                                                                                        training_labels,
                                                                                        test_size=0.2)
    storage_path = os.path.join(directory, ct.name)
    numpy.savez_compressed(storage_path + "_train_images.npz", training_images)
    numpy.savez_compressed(storage_path + "_train_labels.npz", training_labels)
    numpy.savez_compressed(storage_path + "_test_images.npz", testing_images)
    numpy.savez_compressed(storage_path + "_test_labels.npz", testing_labels)


# import skimage.transform
# import numpy
# from sklearn.model_selection import train_test_split
#
# dims = 64
#
#
# def split():
#     katakana = numpy.load("katakana/data/katakana.npz")["arr_0"].reshape([-1, 63, 64]).astype(numpy.float32)
#     katakana = katakana / numpy.max(katakana)
#     training_images = numpy.zeros([51 * 1411, dims, dims], dtype=numpy.float32)
#
#     for i in range(51 * 1411):
#         training_images[i] = skimage.transform.resize(katakana[i], (dims, dims))
#
#     #  51 sets of images, but three sets are duplicates, so 48 classes
#     classes = numpy.arange(51 - 3)
#     duplicates = numpy.array([1, 2, 3])
#     classes = numpy.append(duplicates, classes)
#     classes = numpy.sort(classes)
#     training_labels = numpy.repeat(classes, 1411)
#
#     delete = []
#     for i in range(len(training_images)):
#         if(training_images[i] == numpy.zeros([training_images[i].shape[0], training_images[i].shape[1]], dtype=numpy.uint8)).all():
#             delete.append(i)
#     training_images = numpy.delete(training_images, delete[0], axis=0)
#     training_labels = numpy.delete(training_labels, delete[0])
#
#     training_images = numpy.delete(training_images, delete[1]-1, axis=0)
#     training_labels = numpy.delete(training_labels, delete[1]-1)
#
#
#     training_images, testing_images, training_labels, testing_labels = train_test_split(training_images, training_labels
#                                                                                         , test_size=0.2)
#     numpy.savez_compressed("katakana/data/katakana_train_images.npz", training_images)
#     numpy.savez_compressed("katakana/data/katakana_train_labels.npz", training_labels)
#     numpy.savez_compressed("katakana/data/katakana_test_images.npz", testing_images)
#     numpy.savez_compressed("katakana/data/katakana_test_labels.npz", testing_labels)


# import skimage.transform
# import numpy
# from sklearn.model_selection import train_test_split
#
# dims = 64
#
#
# def split():
#     hiragana = numpy.load("../hiragana.npz")["arr_0"].reshape([-1, 127, 128]).astype(numpy.float32)
#     hiragana = hiragana / numpy.max(hiragana)
#     training_images = numpy.zeros([71 * 160, dims, dims], dtype=numpy.float32)
#
#     for i in range(71 * 160):
#         training_images[i] = skimage.transform.resize(hiragana[i], (dims, dims))
#
#     classes = numpy.arange(71)
#     training_labels = numpy.repeat(classes, 160)
#
#     training_images, testing_images, training_labels, testing_labels = train_test_split(training_images,
#                                                                                         training_labels, test_size=0.2)
#
#     numpy.savez_compressed("../hiragana_train_images.npz", training_images)
#     numpy.savez_compressed("../hiragana_train_labels.npz", training_labels)
#     numpy.savez_compressed("../hiragana_test_images.npz", testing_images)
#     numpy.savez_compressed("../hiragana_test_labels.npz", testing_labels)
