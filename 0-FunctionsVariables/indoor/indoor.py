import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

userInput = input("What do you want to say? ")

indoorVoice = userInput.lower()
print(f"Use your indoor voice! Say: {indoorVoice}")
