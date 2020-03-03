integer = int(input("Please enter an integer: "))
def countingLetters(word):
    string = list(word)
    array1 = string[0::2]
    array2 = string[1::2]
    print(''.join(array1) + ' ' + ''.join(array2))

for _ in range(integer):
    test = str(input("enter a word: "))
    countingLetters(test)


