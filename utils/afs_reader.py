import struct

class AFSEntry:
    
    def __init__(self, offset, lenght):
        self.offset = offset
        self.lenght = lenght

    def __repr__(self) -> str:
        return f"AFSEntry(offset: {self.offset}, lenght: {self.lenght})"

def read_afs_file(file_path) -> "list[bytearray]":
    with open(file_path, 'rb') as f:

        header, num_files = struct.unpack("<4sI",f.read(8))
        if header != b'AFS\x00':
            raise ValueError("El archivo no es un archivo AFS válido.")
                
        afs_entries = []
        
        for _ in range(num_files):
            offset, lenght = struct.unpack("<2I",f.read(8))
            afs_entry = AFSEntry(offset, lenght)
            afs_entries.append(afs_entry)
        
        files = []
        for afs_entry in afs_entries:
            f.seek(afs_entry.offset)
            file_data = f.read(afs_entry.lenght)
            files.append(bytearray(file_data))
        
        return files

if __name__ == "__main__":
    afs_files = read_afs_file("D:\\Juegos\\KONAMI\\Pro Evolution Soccer 5\\dat\\e_text.afs")
    for i, file_data in enumerate(afs_files):
        print(f"Archivo {i}: {len(file_data)} bytes")
