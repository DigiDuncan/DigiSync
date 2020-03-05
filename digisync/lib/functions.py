import xxhash
import digiformatter
import time

BUF_SIZE = 65536  #64kb
BUF_SIZE_KB = BUF_SIZE / 1024

def hash(file):
    start = time.time()
    x = xxhash.xxh64()

    currentKbyte = 0

    print(file)
    print("")

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            x.update(data)
            currentKbyte += BUF_SIZE_KB
            now = time.time()
            offset = now - start
            digiformatter.overwriteLines(2)
            print(f"Hashing... [{currentKbyte:.0f}KB] [{offset:.3f}s]")
    
    return x.hexdigest()