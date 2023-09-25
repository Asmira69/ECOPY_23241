
#GY7EJG
def evens_from_list(input_list):
    return [num for num in input_list if num % 2 == 0]


def every_element_is_odd(input_list):
    for num in input_list:
        if num % 2 == 0:
            return False
    return True


def kth_largest_in_list(input_list, kth_largest):
    if kth_largest <= 0:
        raise ValueError("kth_largest must be a positive integer")

    unique_sorted_list = list(set(input_list))
    unique_sorted_list.sort(reverse=True)

    if kth_largest > len(unique_sorted_list):
        raise ValueError("kth_largest exceeds the number of unique elements in the input list")

    return unique_sorted_list[kth_largest - 1]


def cumavg_list(input_list):
    cumulative_sum = 0
    cumulative_averages = []

    for i, num in enumerate(input_list, start=1):
        cumulative_sum += num
        average = cumulative_sum / i
        cumulative_averages.append(average)

    return cumulative_averages


def element_wise_multiplication(input_list1, input_list2):
    return [x * y for x, y in zip(input_list1, input_list2)]


def merge_lists(*lists):
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    return merged_list


def squared_odds(input_list):
    return [i * i for i in input_list if i % 2 != 0]


def reverse_sort_by_key(input_dict):
    keys = list(input_dict.keys())
    keys.sort(reverse=True)
    reverse_sorted_dict = {i: input_dict[i] for i in keys}
    return reverse_sorted_dict


def sort_list_by_divisibility(input_list):
    by_two = []
    by_five = []
    by_two_and_five = []
    by_none = []

    for num in input_list:
        if num % 2 == 0 and num % 5 == 0:
            by_two_and_five.append(num)
        elif num % 2 == 0:
            by_two.append(num)
        elif num % 5 == 0:
            by_five.append(num)
        else:
            by_none.append(num)

    Dict = {
        'by_two': by_two,
        'by_five': by_five,
        'by_two_and_five': by_two_and_five,
        'by_none': by_none
    }

    return Dict

