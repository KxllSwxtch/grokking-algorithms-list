# Created by Dmitriy Shin on June 18, 2020

def find_smallest(arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallestj))
    return new_arr


arr = [1, 2, 1, 5, 67, 2, 5, 19, 290]
print(selection_sort(arr))
