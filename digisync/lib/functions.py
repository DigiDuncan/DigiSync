import xxhash
import digiformatter
import time
import sys

BUF_SIZE = 65536  #64kb

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
            currentKbyte += sys.getsizeof(data) / 1024
            now = time.time()
            offset = now - start
            digiformatter.overwriteLines(2)
            if currentKbyte > 64:
                print(f"Hashing... [{currentKbyte:.3f}KB] [{offset:.3f}s]")
            else:
                print(f"Hashing... [{currentKbyte * 1024:.0f}B] [{offset:.3f}s]")
    
    return x.hexdigest()