tblOfRates = []
tblOfNames = []

def init():
    nameFile = open("names.txt", "r")
    rateFile = open("rates.txt", "r")

    for line in rateFile:
        tblOfRates.append(line.strip())
   
    for line in nameFile:
        tblOfNames.append(line.strip())

    rateFile.close()
    nameFile.close()

init()

for i in range(len(tblOfNames)):
    print(f"{tblOfNames[i]} gets paid £{tblOfRates[i]} per hour")