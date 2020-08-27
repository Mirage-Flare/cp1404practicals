def main():
    import random
    number_of_scores = int(input("Number of scores: "))
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        score = random.randint(1, 100)
        result = get_result(score)
        print(score,"is", result, file=out_file)
    out_file.close()

def get_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 49:
        return "Passable"
    else:
        return "Bad"


main()
