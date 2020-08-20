"""
Fixing a broken program to determine score status
Kyle Muccignat
"""
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
elif score > 90:
    print("Excellent")
elif score > 49:
    print("Passable")
else:
    print("Bad")
