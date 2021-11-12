import statzcw


def zcorr(listx: list, listy: list) -> float:
    covariance = cov(listx, listy)
    if covariance == "lengths don't match":
        return covariance
    corr = covariance / (statzcw.zstddev(listx) * statzcw.zstddev(listy))
    return corr

def cov(list1: list, list2: list) -> float:
    length = statzcw.zcount(list1)
    if length != statzcw.zcount(list2):
        return "lengths don't match"
    list1_mean = statzcw.zmean(list1)
    list2_mean = statzcw.zmean(list2)
    sum = 0
    i = 0
    while i < length:
        sum += (list1[i] - list1_mean) * (list2[i] - list2_mean)
        i += 1
    return sum / (length - 1)
