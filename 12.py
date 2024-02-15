# numbers = [
# 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
# 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
# 958,743, 527
# ]

# for num in numbers:
#     if num>237:
#         continue
#     else:
#         if num%2 ==0:
#             print(num)

# a = 10
# b = 20

# a, b = b, a

# temp = a
# a = b
# b = temp

# a = a + b
# b = a - b
# a = a - b

# products = ["apple", "cucumber", "grapes"]

# # for loop without enumerate
# for id in range(len(products)):
#     print(len(products) - 1 - id, products[len(products) - 1 - id])

# with enumerate and for loop

# for id, name in enumerate(products):
#     print(id, name)

# # while loop without enumerate

# id = 0

# while id < len(products):
#     print(id, products[id])
#     id += 1

# # while loop with enumerate

# products = list(enumerate(products))

# i = 0
# while i < len(products):
#     id, name = products[i]
#     print(id, name)
#     i += 1


# running sum
# nums = [1, 2, 3, 4, 5]

# sums = []
# for i in range(len(nums)):
#     r_sum = sum(nums[0 : i + 1])
#     sums.append(r_sum)

# print(sums)

# people = [
#     {"name": "mohan", "age": 20},
#     {"name": "vasudha", "age": 58},
#     {"name": "tharani", "age": 66},
#     {"name": "cathy", "age": 15},
#     {"name": "gaytri", "age": 50},
# ]

# for person in people:
#     if person["age"] > 50:
#         print(person["name"])
