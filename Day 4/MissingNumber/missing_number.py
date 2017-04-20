def find_missing(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        list1_length = len(list1)
        list2_length = len(list2)

        # return 0 if the lists are empty
        if list1_length == 0 and list2_length == 0:
            return 0
        else:
            # Convert lists to set data structure because it can get difference between sets
            set_list1 = set(list1)
            set_list2 = set(list2)
            if list1_length > list2_length:
                return list(set_list1 - set_list2).pop()
            elif list2_length > list1_length:
                return list(set_list2 - set_list1).pop()
            else:
                if list(set_list2 - set_list1) == []:
                    return 0
                elif list(set_list2 | set_list1) == list2 and list(set_list2| set_list1) == list1:
                    return 0