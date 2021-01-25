# python3

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    if get_majority_element(elements) == None:
        return 0
    return 1

def get_majority_element(elements):
    n = len(elements)
    if n == 0:
        return
    elif n == 1:
        return elements[0]
    mid_index = n // 2
    left = elements[:mid_index]
    right = elements[mid_index:]

    left = get_majority_element(left)
    right = get_majority_element(right)

    if left == right:
        return left
    elif elements.count(left) > mid_index:
        return left
    elif elements.count(right) > mid_index:
        return right
    return


def majority_element_faster(elements):
    assert len(elements) <= 10 ** 5
    n = len(elements)
    count_dict = dict()
    for element in elements:
        if element in count_dict.keys():
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    mode = max(set(elements), key=elements.count)
    if count_dict[mode] > n/2:
        return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
