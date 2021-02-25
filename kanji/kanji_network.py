from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
import numpy
import os


def train_kanji():
    dims = 64

    training_images = numpy.load("kanji/data/kanji_train_images.npz")["arr_0"]
    training_labels = numpy.load("kanji/data/kanji_train_labels.npz")["arr_0"]
    testing_images = numpy.load("kanji/data/kanji_test_images.npz")["arr_0"]
    testing_labels = numpy.load("kanji/data/kanji_test_labels.npz")["arr_0"]

    print(numpy.max(training_images))
    print(numpy.max(testing_images))
    print(numpy.max(testing_labels))
    print(numpy.max(training_labels))
    for i in training_images:
        if numpy.all((i == 0)):
             print("holy shit")

    training_images = training_images.reshape(training_images.shape[0], dims, dims, 1)
    testing_images = testing_images.reshape(testing_images.shape[0], dims, dims, 1)
    shape = (dims, dims, 1)


    datagen = ImageDataGenerator(rotation_range=45, zoom_range=0.7, rescale=1.0/15.0)
    datagen.fit(training_images)
    print(numpy.max(training_images))

    # model = keras.Sequential([
    #     keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=shape),
    #     keras.layers.MaxPooling2D(2, 2),
    #     keras.layers.Conv2D(64, (3, 3), activation='relu'),
    #     keras.layers.MaxPooling2D(2, 2),
    #     keras.layers.Flatten(),
    #     keras.layers.Dropout(0.5),
    #     keras.layers.Dense(2048, activation='relu'),
    #     keras.layers.Dense(2965, activation="softmax")
    # ])

    model = keras.Sequential([
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu", input_shape=shape, padding="same"),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Dropout(0.2),

        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Dropout(0.2),

        keras.layers.Conv2D(512, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.Conv2D(512, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Dropout(0.2),

        keras.layers.Flatten(),
        keras.layers.Dense(4096, activation="relu"),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.5),

        keras.layers.Dense(2965, activation="softmax")


    ])
    model.summary()
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit_generator(
        datagen.flow(training_images, training_labels, shuffle=True),
        epochs=120,
        validation_data=(testing_images, testing_labels),
        callbacks=[
            keras.callbacks.EarlyStopping(monitor="val_loss", patience=30, verbose=1, restore_best_weights=True)
            # keras.callbacks.ModelCheckpoint("hiragana.h5", monitor="val_loss", save_best_only=True)
        ],
        verbose=2
    )
    test_loss, test_acc = model.evaluate(testing_images, testing_labels)
    print("Test Accuracy: ", test_acc)

    model.save(os.path.join(os.getcwd(), "kanji", "model", "kanji.h5"))