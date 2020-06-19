# Created by Dmitriy Shin on June 19, 2020

def countNumbers(arr: list):
    if not arr:
        return 0
    else:
        return countNumbers(arr[1:]) + 1


if __name__ == '__main__':
    print(countNumbers([1, 2, 3, 4, 5, 6]))
