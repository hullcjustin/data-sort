import math


def merge_sort(data, left, right):
    if left < right:
        midpoint = math.floor((right + left)/2)
        data = merge_sort(data, left, midpoint)
        data = merge_sort(data, midpoint + 1, right)
        data = merge(data, left, right)
    return data


def merge(data, left, right):

    temp_array = []

    midpoint = math.floor((right + left) / 2)
    left_subarray_index = left
    right_subarray_index = midpoint + 1
    while (left_subarray_index <= midpoint) & (int(right_subarray_index) <= int(right)):
        if less_than_or_qual(data[left_subarray_index], data[right_subarray_index]):
            temp_array.append(data[left_subarray_index])
            left_subarray_index += 1
        else:
            temp_array.append(data[right_subarray_index])
            right_subarray_index += 1

    while left_subarray_index <= midpoint:
        temp_array.append(data[left_subarray_index])
        left_subarray_index += 1

    while right_subarray_index <= right:
        temp_array.append(data[right_subarray_index])
        right_subarray_index += 1

    count = 0
    for item in temp_array:
        data[left + count] = item
        count += 1

    return data


def less_than_or_qual(left, right):
    if len(left[0]) <= len(right[0]):
        return True
        #return is_lower_branch(left[0].value, right[0].value)
    else:
        return False


def get_target(row):
    target = row[0].value
    t_count = 0
    count = 0
    for t in target:
        if t == 'T':
            t_count = count

    if isinstance(row[1].value, float):
        item = row[0]
    quote_array = row[1].value.split(" ")
    return quote_array[t_count]


def is_lower_branch(left, right):
    count = 0
    left_location = 0
    right_location = 0
    for l in left:
        if left[count] == 'T':
            left_location = count
    for r in right:
        if right[count] == 'T':
            right_location = count

    if left_location <= right_location:
        return True
    else:
        return False
