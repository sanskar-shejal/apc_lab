import os


def main():
    test_filename = "demo_file_ops.txt"

    print("File Pointer Navigation (tell & seek):")
    with open(test_filename, "w+") as f:
        f.write("Hello Python World! Learning Advance Programming Concepts.")
        print("  Current pointer position after write:", f.tell())
        f.seek(6)
        print("  Pointer position after f.seek(6):", f.tell())
        read_from_6 = f.read(6)
        print("  6 characters read from pos 6:", repr(read_from_6))

    bin_file = "demo_binary.dat"
    print("\nBinary Mode Operations (wb, rb, ab):")
    with open(bin_file, "wb") as bf:
        bf.write(b"Binary Data Header\x00\x01\x02\x03")

    with open(bin_file, "ab") as bf:
        bf.write(b"\nAppended Binary Chunk")

    with open(bin_file, "rb") as bf:
        binary_content = bf.read()
        print("  Binary content read:", binary_content)

    print("\nExclusive Creation Mode ('x'):")
    exclusive_file = "demo_exclusive.txt"
    if os.path.exists(exclusive_file):
        os.remove(exclusive_file)

    try:
        with open(exclusive_file, "x") as ef:
            ef.write("Created with exclusive 'x' mode.")
        print(f"  Successfully created '{exclusive_file}' with 'x' mode.")
    except FileExistsError:
        print(f"  '{exclusive_file}' already exists!")

    print("\nOS Module File System Utilities:")
    print("  Current Working Directory:", os.getcwd())
    print("  Is 'demo_file_ops.txt' a file?:", os.path.isfile(test_filename))
    print("  File size in bytes:", os.path.getsize(test_filename))

    for f in [test_filename, bin_file, exclusive_file]:
        if os.path.exists(f):
            os.remove(f)
    print("  Cleaned up temporary demonstration files.")


if __name__ == "__main__":
    main()
