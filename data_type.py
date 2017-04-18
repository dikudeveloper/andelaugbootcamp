def data_type(some_argument):
    if isinstance(some_argument, str):
        return len(some_argument)
    elif isinstance(some_argument, int):
        return 'no value'

print(data_type(10))
