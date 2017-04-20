class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.length = a

        # Creates a sorted list of numbers using range() in steps of b
        # Super class list contains the sorted list and will be referenced later in search function
        for i in range(self.a):
            list.append(self, self.b)
            self.b += b
            i += 1

    def search(self, value):
        """ Binary Search Algorithm for a value stored in a sorted list"""
        first = 0
        last = self.length - 1
        found = False
        count = 0
        is_found_in_list = False

        try:
            index = self.index(value)
            is_found_in_list = True
        except ValueError:
            index = -1
            is_found_in_list = False

        while first <= last and not found and is_found_in_list and value != self[last]:
            middle_point = (first + last) // 2
            middle_value = self[middle_point]
            if middle_value == value:
                found = True
                count += 1
                index = middle_point
            else:
                if value < middle_value:
                    last = middle_point - 1
                    count += 1
                else:
                    first = middle_point + 1
                    count += 1

        return {"count": count, "index": index}


