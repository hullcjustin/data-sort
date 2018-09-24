import docexe
import merge_sort


def start_sort():
    items_to_sort = docexe.get_openpyxl()
    # for cellObj in sheet['A1': 'C' + str(max_row)]:
    items_to_sort = merge_sort.merge_sort(items_to_sort['items'], 0, len(items_to_sort['items']) - 1)
    data = []
    for item in items_to_sort:
        data.append(item)
    data = sort_list(data)
    return data


def sort_list(item_list):
    # One by one take each item and insert in to sub lists by their Target and target location
    # Sort each sublist, and get ready for print out
    target_dictionary = {'target_freq': 'T',  'target': '-Root-', 'target_list': []}
    for item in item_list:
        if len(item[0]) == 2:

            item_found = False
            for root_item in target_dictionary['target_list']:
                if is_sub_target(item, root_item):
                    root_item['target_list'].append({'target_freq': item[0], 'target': item[1], 'target_list': []})
                    item_found = True
            if not item_found:
                target = get_target(item)
                target_dictionary['target_list'].append(
                    {'target_freq': 'T', 'target': target, 'target_list': [
                        {'target_freq': item[0], 'target': item[1], 'target_list': []}]})
        else:
            for root_key in target_dictionary['target_list']:
                if get_target(item) == get_target(root_key):
                    add_to_dictionary(item, root_key)
    return target_dictionary


def add_to_dictionary(target_tuple, dictionary):
    list_length = len(dictionary['target_list'])
    # what if its empty
    if list_length == 0:
            dictionary['target_list'].append(
                {'target_freq': target_tuple[0], 'target': target_tuple[1], 'target_list': []})
            return dictionary
    if is_sub_target(target_tuple, dictionary):
        item_found = False
        for item in dictionary['target_list']:
            if is_sub_target(target_tuple, item):
                add_to_dictionary(target_tuple, item)
                item_found = True

        if not item_found:
            dictionary['target_list'].append(
                {'target_freq': target_tuple[0], 'target': target_tuple[1], 'target_list': []})
        return dictionary
    else:
        dictionary['target_list'].append(
            {'target_freq': target_tuple[0], 'target': target_tuple[1], 'target_list': []})
        return dictionary


def is_sub_target(item, target_tuple):

    target_phrase = target_tuple['target'].split(" ")
    target_before = words_before_target(target_tuple['target_freq'])
    target_after = words_after_target(target_tuple['target_freq'])
    target_location = get_target_location(target_tuple)

    item_phrase = item[1].split(" ")
    item_before = words_before_target(item[0])
    item_after = words_after_target(item[0])
    item_target_location = get_target_location(item)

    if target_phrase[target_location] != item_phrase[item_target_location]:
        return False

    is_sub_flag = False
    # if target_phrase[0] == '-Root-':
    #   return is_sub_flag
    if (item_before >= target_before) & (item_after >= target_after):
        while target_before > 0:
            if target_phrase[target_location - target_before] != item_phrase[item_target_location - item_before]:
                return is_sub_flag
            target_before -= 1

        while target_after > 0:
            if target_phrase[target_location + target_after] != item_phrase[item_target_location + target_after]:
                return is_sub_flag
            target_after -= 1
        is_sub_flag = True
    return is_sub_flag


def words_after_target(item):
    count = 0
    target_flag = False
    for item_string in item:
        if target_flag:
            count += 1
        if item_string == 'T':
            target_flag = True
    return count


def words_before_target(item):
    count = 0
    for item_string in item[0]:
        if item_string == 'T':
            break
        count += 1
    return count


def get_target_location(item):
    count = 0
    target_array = []
    if 'target_freq' in item:
        target_array = item['target_freq']
    else:
        target_array = item[0]
    for item_string in target_array:
        if item_string == 'T':
            return count
        count += 1


def get_target(item):
    if 'target_freq' in item:
        target_string = item['target']
    else:
        target_string = item[1]

    target_location = get_target_location(item)
    target_array = target_string.split(" ")
    return target_array[target_location]



