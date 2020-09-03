"""
CP1404/CP5632 Practical
Colour to code program
"""

COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                  "DarkGoldenrod": "#b8860b", "DarkGoldenrod1": "#ffb90f", "DarkGreen": "#006400",
                  "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc"}
print(COLOUR_TO_CODE)
colour_name = input("Enter Colour Name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(colour_name, "code is", COLOUR_TO_CODE[colour_name])
    else:
        print("Invalid colour")
    colour_name = input("Enter Colour Name: ")
