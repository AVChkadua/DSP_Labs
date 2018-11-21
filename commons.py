import os


def open_file(filename):
    file = None
    if os.path.isfile(filename):
        print(f"File {filename} exists, overwrite? (y/N)")
        overwrite = input().lower()
        while (overwrite != "y") & (overwrite != "n") & (overwrite != ""):
            print("Input \"y\" or \"n\" (case-insensitive)")
            overwrite = input().lower()
        if (overwrite == "n") | (overwrite == ""):
            print("File will not be overwritten, exiting")
            exit(0)
        else:
            print(f"Overwriting file {filename}")
            file = open(filename, "w")
    else:
        file = open(filename, "w")

    if file is None:
        print("file is None, exiting...")
        exit(1)
    return file
