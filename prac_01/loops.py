"""
Creating loops with range
Kyle Muccignat
"""
# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
user_number = int(input("Number: "))
print("Number of stars: ", user_number)
for number in range(user_number):
    print("*", end ='')

# d.
user_number = int(input("Number: "))
print("Number of stars: ", user_number)
for number in range(user_number + 1):
    print("")
    for number in range(number):
        print("*", end ='')
