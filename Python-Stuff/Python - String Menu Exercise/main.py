name=input("What is your name? ")
pos=name.find("")

print(name.upper())
print(name.lower())
print(name.capitalize())
print(len(name))
print(pos)
print(name.strip())

lastname=name[pos+1:]
print(name[0]+lastname)