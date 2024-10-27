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


def max_difference_02(l: list[int]) -> str:
    if len(l) == 0:
        return "max_difference = 0"

    minimum = l[0]
    maximum = l[0]
    tentative_minimum = l[0]
    _max_difference = maximum - minimum

    for val in l:
        if (val - tentative_minimum) > _max_difference:
            maximum = val
            minimum = tentative_minimum
            _max_difference = maximum - minimum
        elif val < tentative_minimum:
            tentative_minimum = val

    # _max_difference = maximum - minimum
    # res = f"max_difference = {_max_difference} ({high_val} (at index {high_index}) - {low_val} (at index {low_index}))"
    res = f"max_difference = {_max_difference} ({maximum} - {minimum})"
    return res


def main() -> None:
    print(max_difference_02([2, 3, 10, 6, 4, 8, 1]))


if __name__ == '__main__':
    main()


# -- C++ code from discord --
#
# int max_difference(const vector<int>& numbers) {
#     if (numbers.size() == 0) return 0;

#     int minimum = numbers[0];
#     int maximum = numbers[0];
#     int tentative_minimum = numbers[0];
#     for (unsigned int i = 1; i < numbers.size(); i++) {
#         if ((numbers[i] - tentative_minimum) > (maximum - minimum)) {
#             maximum = numbers[i];
#             minimum = tentative_minimum;
#         } else if (numbers[i] < tentative_minimum) {
#             tentative_minimum = numbers[i];
#         }
#     }

#     return maximum - minimum;
# }
