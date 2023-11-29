#Brug af index på lister
mylist = ["Lasse", "Anders", "Peter", "Lasse"]
print(mylist[2])
print("Hvorfor er det Peter der udskrives?")
print()

#negativ index tal
mylist = ["Lasse", "Anders", "Peter", "Lasse", "Kurt", "Jens"]
#Nu udskrives det sidste element i listen
print(mylist[-1])
print()
#hvad udskrives nu?
print(mylist[-2])
#Nu udskrives elementer i listen
print("for løkken udskrives nu!")
for mitElement in mylist:
    print(mitElement)

#Udskriver en del af listen
print(mylist[:2])

for n in range(2,5):
    print(mylist[n])



