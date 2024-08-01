fo = open("lkfile.txt", "r+")
for line in fo.readlines(): # læser al tesksten i en file til enden af filen
   print(f"Læser: {line}")