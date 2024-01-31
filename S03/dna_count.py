
seq = ""
sequence = True
while sequence:
    seq = input("Please enter a sequence: ")
    if (len(seq . replace("A" , "") . replace("C" , "") . replace("G" , "") . replace("T" , "")) == 0) == False:
        print("The sequence is correct")
        sequence = False
    else:
        print("The sequence is incorrect")

numberA = 0
numberC = 0
numberG = 0
numberT = 0
length =  len(seq)
print("Total length: " , length)
for character in seq.upper():
    if character == "A":
        numberA += 1
    elif character == "C":
        numberC += 1
    elif character == "G":
        numberG += 1
    elif character == "T":
        numberT += 1
print("Number of times that letter 'A' appears in the sentence:",numberA)
print("Number of times that letter 'C' appears in the sentence:",numberC)
print("Number of times that letter 'G' appears in the sentence:",numberG)
print("Number of times that letter 'T' appears in the sentence:",numberT)