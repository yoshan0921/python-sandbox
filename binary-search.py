import random

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
    print("Please input the number of data.")
    num_data = int(input())   
    data = [random.randint(0, 10000) for i in range(num_data)]
    print(data)

    print("Please select on of the numbers.")
    value = int(input())
    result = binary_search(data, value)
    print(result)

