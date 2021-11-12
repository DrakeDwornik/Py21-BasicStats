import statzcw

def zstddev(list: list) -> float:
    variance = statzcw.zvariance(list)
    stddev = variance ** .5
    return stddev