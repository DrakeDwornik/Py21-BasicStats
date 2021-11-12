import statzcw


def zmedian(list: list) -> float:
    length = statzcw.zcount(list)
    sorted_list = bubble_sort_list(list, length)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        mean_of_middle_two = (sorted_list[length // 2] + sorted_list[(length // 2) - 1]) / 2
        return mean_of_middle_two


def bubble_sort_list(input_list: list, list_length: int) -> list:
    swap = True
    while swap:
        swap = False
        current = 0
        while current < list_length - 1:
            if input_list[current] > input_list[current + 1]:
                input_list[current + 1], input_list[current] = (input_list[current], input_list[current + 1])
                swap = True
            current += 1
    return input_list

if __name__ == '__main__':
    pass