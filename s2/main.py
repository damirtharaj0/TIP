

# # U: The elements in the rows become the elements in the columns.

# # P: populate another matrix with 0 and then go through the matrix and swap the indicies

# # I:
# '''
# prepopulate a new matrix

# nested for loop
#   swap indicies

# return new matrix

# '''

# def transpose(matrix):
#     new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

#     rows = len(matrix)
#     cols = len(matrix[0])

#     for i in range(rows):
#         for j in range(cols):
#             new_matrix[j][i] = matrix[i][j]

#     return new_matrix


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(transpose(matrix))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(transpose(matrix))


"""
U: reverse the list using two pointers

P: left pointer at beginning, right at the end.
increment left and decrement right until l >= right
swap the elements

"""

# def reverse_list(lst):
#     l, r = 0, len(lst) - 1

#     while l < r:
#         lst[l], lst[r] = lst[r], lst[l]
#         l += 1
#         r -= 1

# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# reverse_list(lst)
# print(lst)


"""
U: remove the duplicates

P: Left and right pointer left is the list without duplicates. right scans through the array.
If a right values is alreadu im the set, don't increment the elft.
else 

seen = set("extract of malt",  "haycorns", "honey", "thistle" )
["extract of malt", "haycorns", "honey", "thistle", "thistle"]
l = 3

I:
"""


# def remove_dupes(items):
#     if len(items) < 2:
#         return items
#     l, r = 0, 1

#     while r < len(items):
#         if items[r] == items[l]:
#             items.remove(items[r])
#         else:
#             l = r
#         r += 1

#     return items


# # items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# # print(remove_dupes(items))

# items = ["extract of malt", "haycorns", "haycorns", "honey", "thistle"]
# print(remove_dupes(items))



def sort_by_parity(nums):
    l, r = 0, len(nums) - 1

    for i, num in enumerate(nums):
        if num % 2 == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        else:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1

nums = [3, 1, 2, 4]
sort_by_parity(nums)

print(nums)