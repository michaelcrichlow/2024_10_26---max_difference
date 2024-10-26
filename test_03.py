def max_difference(l: list[int]) -> str:
    _max_difference = 0
    low_index = 0
    high_index = 0
    low_val = 0
    high_val = 0

    for i in range(len(l) - 1):
        num = 1
        while (i + num) < len(l):
            if l[i + num] > l[i]:
                if l[i + num] - l[i] > _max_difference:
                    low_index = i
                    high_index = i + num
                    low_val = l[i]
                    high_val = l[i + num]
                    _max_difference = high_val - low_val

            num += 1

    res = f"max_difference = {_max_difference} ({high_val} (at index {high_index}) - {low_val} (at index {low_index}))"
    return res


def main() -> None:
    print(max_difference([2, 3, 10, 6, 4, 8, 1]))


if __name__ == '__main__':
    main()
