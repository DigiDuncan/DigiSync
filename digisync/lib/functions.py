import xxhash
import digiformatter
import time
import sys

from digisync.lib.format import formatByteSize, formatTimeDelta

BUF_SIZE = 65536  # 64kb


def hash(file, debug = False):
    start = time.time()
    x = xxhash.xxh64()

    currentbyte = 0
    lastsecond = None

    print(digiformatter.truncate(file, 80, True))

    if debug:
        print("Hashing...\nSpeed", end = "")

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            x.update(data)
            currentbyte += sys.getsizeof(data)
            now = time.time()
            offset = now - start
            if debug:
                digiformatter.overwriteLines(2)
                print(f"Hashing... [{formatByteSize(currentbyte)}] [{formatTimeDelta(offset)}]")
                if lastsecond is None or now - lastsecond >= 1:
                    try:
                        speed = formatByteSize(currentbyte / offset)
                    except ZeroDivisionError:
                        speed = "∞"
                    print(f"{speed}/s", end = "")
                if lastsecond is not None:
                    if now - lastsecond >= 1:
                        lastsecond = now
                else:
                    lastsecond = now
    print("")
    return x.hexdigest()


def readINI(ini):
    # Returns a dictionary of value pairs.
    # I'm making this function from scratch
    # because the built in one screws up with
    # duplicate keys and a bunch of the inis
    # in the dataset are malformed like that.

    inif = open(ini)
    lines = inif.readlines()
    # TODO: Do stuff...
    inif.close()
