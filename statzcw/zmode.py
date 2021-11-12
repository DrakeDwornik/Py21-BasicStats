def zmode(list: list) -> float:
    values = {}
    for item in list:
        try:
            values[item] += 1
        except:
            values[item] = 1

    mode = 0
    for key in values:
        if values[key] > mode:
            mode = key
    return(mode)


if __name__ == '__main__':
    print(zmode([1,2,2,3,3,3,3]))
