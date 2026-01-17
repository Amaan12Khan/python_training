list_a = [1, 2, 3, 2, 1]

left = 0
right = len(list_a) - 1

while left < right:
    if list_a[left] != list_a[right]:
        print("The list is not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print("The list is a palindrome.")