from sklearn.model_selection import train_test_split
import numpy
import os
import skimage.transform as skitr


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
    print(numpy.max(kanji))
    # kanji = kanji / numpy.max(kanji)
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

