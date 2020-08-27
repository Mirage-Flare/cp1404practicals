# Code used to create the temps_input.txt file
# out_file = open("temps_input.txt", "w")
# import random
# for i in range(15):
#     print(random.uniform(-200, 200), file=out_file)
# out_file.close()


def main():
    out_file = open("temps_output.txt", "w")
    in_file = open("temps_input.txt", "r")
    for line in in_file:
       fahrenheit = float(line)
       celsius = convert_f_to_c(fahrenheit)
       print(celsius, file=out_file)
    out_file.close()
    in_file.close()


def convert_f_to_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
