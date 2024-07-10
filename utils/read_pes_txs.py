import struct, io
from utils.constants import *
from classes.texture_file import TextureFile

def read_pes_txs(file_number:int, file_io:io.BytesIO):
    txs_info:"list[str]" = []
    current_file_name = f"unknow_{file_number:05}"
    
    magic_number, file_size = struct.unpack("<2I", file_io.read(8))
    if magic_number != TXS_MAGIC_NUMBER: return None
    file_io.seek(HEADER_SIZE, 0)
    file_with_no_header = io.BytesIO(file_io.read(file_size))
    total_files, offset_filename_table, offset_file_data_table = struct.unpack("<3I", file_with_no_header.read(12))
            
    texture_files:"list[TextureFile]" = [TextureFile()] * total_files
    
    for i, texture_file in enumerate(texture_files):
        file_with_no_header.seek(offset_filename_table + i * 4)
        offset = struct.unpack("<I", file_with_no_header.read(4))[0]
        texture_file.get_filename_from_offset(file_with_no_header, offset)
        file_with_no_header.seek(offset_file_data_table + i * 4)
        offset = struct.unpack("<I", file_with_no_header.read(4))[0]
        texture_file.get_file_data_from_offset(file_with_no_header, offset)
        txs_idx_bytes = texture_file.decompress()[12:16]
        txs_idx_int = struct.unpack("<I", txs_idx_bytes)[0]
        print("Parent file: %s, TXS Name: %s, Integer Value: %d" % (current_file_name, texture_file.file_name, txs_idx_int))
        txs_info.append(f"{current_file_name},{texture_file.file_name},{txs_idx_int}\n")
    return txs_info

