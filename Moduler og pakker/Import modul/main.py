""" Dokumentationen for Mit_modul.py som indeholder funktionen hello_world
"""
import Mit_modul
import Nyt_modul

name = input("Indtast dit navn her ")
Mit_modul.hello_world(name)

if __name__ == '__main__':
    print(__name__)
x = int(input("Indtast et tal?"))
y = int(input("Indtast et nyt tal der skal ganges med hinanden"))
Mit_modul.regne(x, y)

Nyt_modul.musik()
