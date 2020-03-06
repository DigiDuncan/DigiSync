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

def formatTimeDelta(totalSeconds, millisecondAccuracy = True):
    MILLISECONDS_PER_SECOND = 1000
    MILLISECONDS_PER_MINUTE = MILLISECONDS_PER_SECOND * 60
    MILLISECONDS_PER_HOUR = MILLISECONDS_PER_MINUTE * 60
    MILLISECONDS_PER_DAY = MILLISECONDS_PER_HOUR * 24
    MILLISECONDS_PER_YEAR = MILLISECONDS_PER_DAY * 365

    milliseconds = int(totalSeconds * 1000)
    totalmilliseconds = milliseconds
    years, milliseconds = divmod(milliseconds, MILLISECONDS_PER_YEAR)
    days, milliseconds = divmod(milliseconds, MILLISECONDS_PER_DAY)
    hours, milliseconds = divmod(milliseconds, MILLISECONDS_PER_HOUR)
    minutes, milliseconds = divmod(milliseconds, MILLISECONDS_PER_MINUTE)
    seconds, milliseconds = divmod(milliseconds, MILLISECONDS_PER_SECOND)

    s = ""
    if totalmilliseconds >= MILLISECONDS_PER_YEAR:
        s += f"{years:d}y"
    if totalmilliseconds >= MILLISECONDS_PER_DAY:
        s += f"{days:d}d"
    if totalmilliseconds >= MILLISECONDS_PER_HOUR:
        s += f"{hours:0>2d}h"
    if totalmilliseconds >= MILLISECONDS_PER_MINUTE:
        s += f"{minutes:0>2d}m"
    if millisecondAccuracy:
        s += f"{seconds:0>2d}.{milliseconds:0>3d}s"
    else:
        s += f"{seconds:0>2d}s"

    return s