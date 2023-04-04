import random


def generate_random_list(n, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]


def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle_index = len(numbers) // 2
    left_half = numbers[:middle_index]
    right_half = numbers[middle_index:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])
    return result


random_numbers = generate_random_list(10, 1, 100)
print(f"Original list: {random_numbers}")
sorted_numbers = bubble_sort(random_numbers)
print(f"Sorted list using bubble sort: {sorted_numbers}")
random_numbers = generate_random_list(10, 1, 100)
print(f"Original list: {random_numbers}")
sorted_numbers = merge_sort(random_numbers)
print(f"Sorted list using merge sort: {sorted_numbers}")
