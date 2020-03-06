import xxhash
import digiformatter
import time
import sys

from digisync.lib.format import formatByteSize, formatTimeDelta

BUF_SIZE = 65536  #64kb

def hash(file, debug = False):
    start = time.time()
    x = xxhash.xxh64()

    currentbyte = 0

    print(file)
    if debug:
        print("")

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            x.update(data)
            currentbyte += sys.getsizeof(data)
            now = time.time()
            offset = now - start
            digiformatter.overwriteLines(2)
            if debug:
                print(f"Hashing... [{formatByteSize(currentbyte)}] [{formatTimeDelta(offset)}]")
    
    return x.hexdigest()