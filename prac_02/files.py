# 1.
# out_file = open("name.txt", "w")
# name = input("Name: ")
# print(name, file=out_file)
# out_file.close()

#  2.
# in_file = open("name.txt", "r")
# name = in_file.read().strip()
# print("Your name is", name)
# in_file.close()

#  3.
# in_file = open("numbers.txt", "r")
# first_number = int(in_file.readline())
# second_number = int(in_file.readline())
# print(first_number + second_number)
# in_file.close()

# 4.
# in_file = open("numbers.txt", "r")
# total = 0
# for line in in_file:
#     number = int(line)
#     total += number
# print(total)
# in_file.close()
