import struct, zlib
from utils.constants import *

class TextureFile():
    file_name = ""
    file_data = bytearray()
    file_data_size = 0
    file_data_decompress = 0
    
    def get_filename_from_offset(self, file, offset):
        file.seek(offset)
        tmp = file.read()
        self.file_name = tmp.partition(bytearray([0x00]))[0].decode("utf8")

    def get_file_data_from_offset(self, file, offset):
        file.seek(offset)
        tmp = file.read()
        magic_number, self.file_data_size, self.file_data_decompress = struct.unpack("<3I", tmp[:12])
        if magic_number != 0x00010300: return
        self.file_data = tmp[: HEADER_SIZE + self.file_data_size]

    def decompress(self):
        decompressed_bytes = zlib.decompress(self.file_data[HEADER_SIZE:])
        if self.file_data_decompress != len(decompressed_bytes): raise Exception("Error while decompressing!!! size doesn't match")
        return decompressed_bytes
