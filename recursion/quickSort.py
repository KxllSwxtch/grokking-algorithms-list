# Created by Dmitriy Shin on June 19, 2020

def quicksort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [j for j in arr[1:] if j > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([4, 5, 1, 2, 3, 5]))
