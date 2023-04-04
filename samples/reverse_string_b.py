def reverse(string):
  reversed_string = ""
  for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]
  return reversed_string

print(reverse("hello"))
