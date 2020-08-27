"""
Fixing a broken program to determine score status
Kyle Muccignat
"""


def main():
    import random
    score = float(input("Enter score: "))
    result(score)
    print(result(score))
    score = random.randint(1,100)
    print(result(score))


def result(score):
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
