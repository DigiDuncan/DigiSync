import xxhash
import digiformatter

BUF_SIZE = 65536  #64kb

def hash(file):
    x = xxhash.xxh64()

    currentbyte = 0

    print(file)
    print("")

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            x.update(data)
            currentbyte += BUF_SIZE
            digiformatter.overwriteLines(2)
            print(f"Hashing... [{currentbyte} bytes]")
    
    return x.hexdigest()