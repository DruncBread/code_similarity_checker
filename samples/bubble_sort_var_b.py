import random

def generate_random_list(n, lower_bound, upper_bound):
  return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def bubble_sort(nums):
  for i in range(len(nums)):
    for j in range(len(nums)-1):
      if nums[j] > nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]
  return nums


def merge_sort(nums):
  if len(nums) <= 1:
    return nums

  middle_index = len(nums) // 2
  left_half = nums[:middle_index]
  right_half = nums[middle_index:]

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


random_nums = generate_random_list(10, 1, 100)
print(f"Original list: {random_nums}")
sorted_nums = bubble_sort(random_nums)
print(f"Sorted list using bubble sort: {sorted_nums}")
random_nums = generate_random_list(10, 1, 100)
print(f"Original list: {random_nums}")
sorted_nums = merge_sort(random_nums)
print(f"Sorted list using merge sort: {sorted_nums}")
