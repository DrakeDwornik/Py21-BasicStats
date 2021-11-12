import statzcw
def zvariance(list):
    count = statzcw.zcount(list)
    mean = statzcw.zmean(list)
    deviations = []
    squared_deviations = []
    for value in list:
        value_deviation = value - mean
        deviations += [value_deviation]
    for deviation in deviations:
        squared_deviation = deviation * deviation
        squared_deviations += [squared_deviation]
    squared_sum = sum(squared_deviations)
    sample_variance = squared_sum  / (count - 1)
    return sample_variance

if __name__ == '__main__':
    print(zvariance([1,2,3,4,5]))