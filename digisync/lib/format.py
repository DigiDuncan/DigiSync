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
    MILLISECONDS_PER_YEAR = 86400 * 365 * 1000
    MILLISECONDS_PER_DAY = 86400 * 1000
    MILLISECONDS_PER_HOUR = 3600 * 1000
    MILLISECONDS_PER_MINUTE = 60 * 1000
    MILLISECONDS_PER_SECOND = 1000

    milliseconds = int(totalSeconds * 1000)
    years, milliseconds = divmod(milliseconds, MILLISECONDS_PER_YEAR)
    days, milliseconds = divmod(milliseconds, MILLISECONDS_PER_DAY)
    hours, milliseconds = divmod(milliseconds, MILLISECONDS_PER_HOUR)
    minutes, milliseconds = divmod(milliseconds, MILLISECONDS_PER_MINUTE)
    seconds, milliseconds = divmod(milliseconds, MILLISECONDS_PER_SECOND)

    s = ""
    if totalSeconds >= MILLISECONDS_PER_YEAR:
        s += f"{years:d}y"
    if totalSeconds >= MILLISECONDS_PER_DAY:
        s += f"{days:d}d"
    if totalSeconds >= MILLISECONDS_PER_HOUR:
        s += f"{hours:d}h"
    if totalSeconds >= MILLISECONDS_PER_MINUTE:
        s += f"{minutes:d}m"
    if millisecondAccuracy:
        s += f"{seconds:d}.{milliseconds:d}s"
    else:
        s += f"{seconds:d}s"

    return s