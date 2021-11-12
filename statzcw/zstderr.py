import statzcw

def zstderr(list):
    count = statzcw.zcount(list)
    stddev = statzcw.zstddev(list)
    stderr = stddev / count ** .5
    return stderr