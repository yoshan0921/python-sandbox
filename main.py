def binary_search(data: list, value: int):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid -1
    return -1

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70, 80]
    result = binary_search(data, 40)
    print(result)

