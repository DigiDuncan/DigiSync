from digisync.lib.functions import hash

testfile = "C:\\Users\\digid\\Desktop\\RSBE01.wbfs"

def main():
    instring = input("Input a file to hash: ")
    if instring == "":
        instring = testfile
    print(hash(instring, debug = True))