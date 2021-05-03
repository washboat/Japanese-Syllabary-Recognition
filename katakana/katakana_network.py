from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
import numpy
import os

#
# builds and trains convolutional neural network for recognition of katakana
# model input is expected to be 64x64 in size
#

def train_katakana():
    dims = 64

    training_images = numpy.load("katakana/data/katakana_train_images.npz")["arr_0"]
    training_labels = numpy.load("katakana/data/katakana_train_labels.npz")["arr_0"]
    testing_images = numpy.load("katakana/data/katakana_test_images.npz")["arr_0"]
    testing_labels = numpy.load("katakana/data/katakana_test_labels.npz")["arr_0"]


    training_images = training_images.reshape(training_images.shape[0], dims, dims, 1)
    testing_images = testing_images.reshape(testing_images.shape[0], dims, dims, 1)
    dimensions = (dims, dims, 1)

    datagen = ImageDataGenerator(rotation_range=45, zoom_range=0.7)
    datagen.fit(training_images)

    model = keras.Sequential([
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu", input_shape=dimensions, padding="same"),
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Dropout(0.2),

        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Dropout(0.2),

        keras.layers.Conv2D(256, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.Conv2D(256, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Dropout(0.2),

        keras.layers.Conv2D(512, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.Conv2D(512, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.Conv2D(512, kernel_size=(3, 3), activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Dropout(0.2),

        keras.layers.Flatten(),
        keras.layers.Dense(4096, activation="relu"),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.5),

        keras.layers.Dense(46, activation="softmax"),
    ])
    model.summary()
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit_generator(
        datagen.flow(training_images, training_labels, shuffle=True),
        epochs=120,
        validation_data=(testing_images, testing_labels),
        callbacks=[
            keras.callbacks.EarlyStopping(monitor="val_loss", patience=10, verbose=1, restore_best_weights=True)
        ],
        verbose=2
    )
    test_loss, test_acc = model.evaluate(testing_images, testing_labels)
    model.save(os.path.join(os.getcwd(), "katakana", "model", "katakana.h5"))
    print("Test Accuracy: ", test_acc)
