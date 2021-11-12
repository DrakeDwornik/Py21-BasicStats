import statzcw

def zmean(list: list) -> float:
    items_count = statzcw.zcount(list)
    items_sum = sum(list)
    return items_sum / items_count


if __name__ == '__main__':
    print(statzcw.zmean([1,2]))