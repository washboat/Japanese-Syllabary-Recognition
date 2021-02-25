from PIL import Image
import struct


def read_next(file, metadata):
    resolution = metadata.resolution
    buffer_size = metadata.buffer
    format_string = metadata.format
    image_index = metadata.image_data_index
    bit_depth = metadata.depth

    buffer = file.read(buffer_size)
    unpacked = struct.unpack(format_string, buffer)
    image = Image.frombytes("F", resolution, unpacked[image_index], "bit", bit_depth)
    converted_image = image.convert("L")

    return unpacked[metadata.jis_code_index], converted_image, unpacked[1]
