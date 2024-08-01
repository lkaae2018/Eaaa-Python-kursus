# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Close opend file
fo.close()
print(f"Closed or not : {fo.closed}")
