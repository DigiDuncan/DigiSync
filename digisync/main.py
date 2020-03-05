from digisync.lib.functions import hash

def main():
    instring = input("Input a file to hash: ")
    print(hash(instring))