#GY7EJG
#1
def evens_from_list(input_list):
    even = [num for num in input_list if num % 2 == 0]
    return even

#2
def every_element_is_odd(input_list):
    for num in input_list:
        if num % 2 == 0:
            return False
    return True

#3
def kth_largest_in_list(input_list, kth_largest):
    if kth_largest <= 0 or kth_largest > len(input_list):
        raise ValueError("Érvénytelen k érték.")

    sorted_list = sorted(input_list, reverse=True)

    kth_largest_element = sorted_list[kth_largest - 1]

    return kth_largest_element

#4
def cumavg_list(input_list):
    cumulative_sum = 0
    cumulative_average = []

    for i, num in enumerate(input_list, 1):
        cumulative_sum += num
        average = cumulative_sum / i
        cumulative_average.append(average)

    return cumulative_average

#5
def element_wise_multiplication(input_list1, input_list2):
    if len(input_list1) != len(input_list2):
        raise ValueError("A ket lista hossza eltero.")

    result = [x * y for x, y in zip(input_list1, input_list2)]
    return result

#6
def merge_lists(*lists):
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    return merged_list

#7
def squared_odds(input_list):
    squared_odds_list = [x**2 for i in input_list if i % 2 != 0]
    return squared_odds_list

#8
def reverse_sort_by_key(input_dict):
    keys = list(input_dict.keys())
    keys.sort(reverse = True)
    sorted_dict = {i:input_dict[i] for i in keys}
    return sorted_dict

#9
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