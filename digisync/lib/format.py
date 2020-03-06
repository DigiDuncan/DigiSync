def formatByteSize(byteamount: int):
    # Technically this is returning it in kibibytes, etc.,
    # but claims it's in kilobytes etc. Windows does this
    # so it's fine.

    prefixes = ["K", "M", "G", "T", "P"]

    if byteamount < 1024:
        return f"{byteamount}B"

    for i in range(len(prefixes)):
        byteamount /= 1024
        if byteamount < 1024:
            return f"{byteamount:.3f}{prefixes[i]}B"

    return f"{byteamount:.3f}EB"