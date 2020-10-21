    #split numbers' digits
    # lopp through each digit and add
    # check if new number is more than two digits
    # if yes, loop and add, if no, reutrn number of loops
    #counter for loops

    #linked list?

def additivePersistence(input): #13
    loopCounter = 0
    # this adds the digits in the numbers
    total = 0
    splitNum = list(map(int,str(input))) # [1, 3]
    print(splitNum)
    for thing in splitNum:
        total = total + thing
    print(total)

    

print(additivePersistence(199))
