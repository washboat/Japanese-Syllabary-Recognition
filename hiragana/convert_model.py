import tensorflow
import os
from tensorflow import keras
from tflite_support import flatbuffers
from tflite_support import metadata as _metadata
from tflite_support import metadata_schema_py_generated as _metadata_fb


def convert():

    path = os.path.join(os.getcwd(), "../Models", "best_hiragana.h5")
    model = keras.models.load_model(path)
    converter = tensorflow.lite.TFLiteConverter.from_keras_model(model)
    lite_model = converter.convert()
    open("../converted_model.tflite", "wb").write(lite_model)

    model_meta = _metadata_fb.ModelMetadataT()
    model_meta.name = "Hiragana image classifier"
    model_meta.description = "Identify 71 hiragana characters including the gojūon, dakuon, and handakuon characters"
    model_meta.version = "v1"
    model_meta.author = "Triston Gregoire"

    input_meta = _metadata_fb.TensorMetadataT()
    input_meta.name = "image"
    input_meta.description = "Input image to be classified. Image is grayscale with expected dimensions of {0}x{1}.".format(64, 64)
    input_meta.content = _metadata_fb.ContentT()
    input_meta.content.contentProperties = _metadata_fb.ImagePropertiesT()
    input_meta.content.contentProperties.colorSpace = _metadata_fb.ColorSpaceType.GRAYSCALE
    input_meta.content.contentPropertiesType = _metadata_fb.ContentProperties.ImageProperties

    input_normalization = _metadata_fb.ProcessUnitT()
    input_normalization.optionsType = _metadata_fb.ProcessUnitOptions.NormalizationOptions
    input_normalization.options = _metadata_fb.NormalizationOptionsT()
    input_normalization.options.mean = [0.5]
    input_normalization.options.std = [0.5]
    input_meta.processUnits = [input_normalization]

    input_stats = _metadata_fb.StatsT()
    input_stats.max = [1.0]
    input_stats.min = [0.0]
    input_meta.stats = input_stats

    output_meta = _metadata_fb.TensorMetadataT()
    output_meta = _metadata_fb.TensorMetadataT()
    output_meta.name = "probability"
    output_meta.description = "Probabilities of the 71 labels respectively."
    output_meta.content = _metadata_fb.ContentT()
    output_meta.content.contentProperties = _metadata_fb.FeaturePropertiesT()
    output_meta.content.contentPropertiesType = _metadata_fb.ContentProperties.FeatureProperties

    output_stats = _metadata_fb.StatsT()
    output_stats.max = [1.0]
    output_stats.min = [0.0]
    output_meta.stats = output_stats

    # label_file = _metadata_fb.AssociatedFileT()
    # label_file.name = os.path.basename("your_path_to_label_file")
    # label_file.description = "Labels for objects that the model can recognize."
    # label_file.type = _metadata_fb.AssociatedFileType.TENSOR_AXIS_LABELS
    # output_meta.associatedFiles = [label_file]

    subgraph = _metadata_fb.SubGraphMetadataT()
    subgraph.inputTensorMetadata = [input_meta]
    subgraph.outputTensorMetadata = [output_meta]
    model_meta.subgraphMetadata = [subgraph]

    b = flatbuffers.Builder(0)
    b.Finish(model_meta.Pack(b), _metadata.MetadataPopulator.METADATA_FILE_IDENTIFIER)
    metadata_buf = b.Output()

    populator = _metadata.MetadataPopulator.with_model_file(os.path.join(os.getcwd(), "../converted_model.tflite"))
    populator.load_metadata_buffer(metadata_buf)
    # populator.load_associated_files("your_path_to_label_file")
    populator.populate()


