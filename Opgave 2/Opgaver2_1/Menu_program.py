#Lav et menu program med 3 punkter i
# 1) Frem
# 2) Tilbage
# 3) Stop
# og få den til at skifte mellem de 3 menupunkter.
valg =0

def menu():
    global valg
    print("1) Frem, 2) Tilbage, 3) Stop")
    valg=int(input("Indtast dit valg?"))

menu()

while valg==1:
    print("Du har valgt menu nr. 1")
    menu()

while valg==2:

while valg==3:

    break
