# Statemachine til beskrivelse af livets gang
import time


def Home(x):
    if x == "wake":
        x = "take train"
        print("Tager toget på arbejde")
        time.sleep(1)
        return Work(x)
    elif x == "take train":
        x = "sleep"
        print("Går i seng")
        time.sleep(1)
        return Bed(x)


def Work(x):


def Bed(x):


state = Home(x="wake")
while state: state = Home(x="wake")
print("Død og færdig!!!!")
