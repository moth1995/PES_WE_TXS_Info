import sys, io
from pathlib import Path
from utils.read_pes_txs import read_pes_txs
from utils.afs_reader import read_afs_file

def main():
    total_arg = len(sys.argv)
    if total_arg != 2:
        print("Invalid quantity of elements, you just need to give the path for your afs file")
        return

    file_path = Path(str(sys.argv[1]))
    filename = file_path.stem
    full_filename = file_path.resolve()
    csv_filename = file_path.parent.joinpath(f"{filename}_txs_info.csv")

    files_in_afs = read_afs_file(full_filename)

    with open(csv_filename, "w") as csv_file:
        csv_file.write("PARENT FILE,TXS NAME,TXS ID\n")

        for file_number, file_bytes in enumerate(files_in_afs):
            if len(file_bytes) < 8: continue
            file_io = io.BytesIO(file_bytes)
            txs_info = read_pes_txs(file_number, file_io)
            if txs_info is None: continue
            csv_file.writelines(txs_info)
    input("Press enter to exit")

if __name__ == "__main__":
    main()
