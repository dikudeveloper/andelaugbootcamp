def find_max_min(a_list):
    if isinstance(a_list, list):
        is_valid = False
        for i in a_list:
            if isinstance(i, int) or isinstance(i, float):
                is_valid = True
        if is_valid:
            min_value = min(a_list)
            max_value = max(a_list)
            if min_value == max_value:
                return [a_list.count(min_value)]
            else:
                return [min_value, max_value]
