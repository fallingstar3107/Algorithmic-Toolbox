# python3
def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):

    min_index = 0
    max_index = len(keys) - 1

    while max_index >= min_index:
        mid_index = int((max_index + min_index) / 2)
        if keys[mid_index] == query:
            return mid_index
        elif keys[mid_index] < query:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
