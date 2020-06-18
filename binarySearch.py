# Created by Dmitriy Shin on June 18, 2020

def binarySearch(arr: list, item) -> bool:
    '''
    An implementation of a binary search algorithm
    Make sure the argument 'arr' passed is sorted
    '''
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


my_list = [1, 2, 4, 6, 12, 23]
my_list.sort()
print(binarySearch(my_list, 2))
