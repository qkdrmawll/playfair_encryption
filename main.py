def convertPlainTextToDiagraphs (plainText,char1,char2):


    for s in range(0,len(plainText)+1,2):
        if s<len(plainText)-1:
            if plainText[s]==plainText[s+1]:
                plainText = plainText[:s+1]+'X'+plainText[s+1:]
            if plainText[s]==char1 and plainText[s+1]==char2:
                plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]


    if len(plainText)%2 != 0:
        plainText = plainText[:]+'X'

    return plainText

def generateKeyMatrix (key, char1, char2):

    matrix_5x5 = [[0 for i in range (5)] for j in range(5)]

    key=key.replace(char2,char1)

    simpleKeyArr = []

    is_char1_exist = char1 in simpleKeyArr

    for c in key:
        if c not in simpleKeyArr:
            if c == char2 and not is_char1_exist:
                simpleKeyArr.append(char1)
                is_char1_exist = True
            elif c == char1:
                simpleKeyArr.append(c)
                is_char1_exist = True
            else:
                simpleKeyArr.append(c)

    for i in range(65,91):
        if chr(i) not in simpleKeyArr:

            if i==ord(char1) and not is_char1_exist:
                simpleKeyArr.append(char1)
                is_char1_exist = True
            elif i==ord(char1) or i==ord(char2) and is_char1_exist:
                pass
            else:
                simpleKeyArr.append(chr(i))

    index = 0
    for i in range(0,5):
        for j in range(0,5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index+=1

    for i in range(0,5):
        for j in range(0,5):
            print(matrix_5x5[i][j], end="  ")
        print("\n")
    return matrix_5x5

def indexLocator (char,cipherKeyMatrix,char1,char2):
    indexOfChar = []

    if char==char2:
        char = char1

    for i,j in enumerate(cipherKeyMatrix):

        for k,l in enumerate(j):

            if char == l:
                indexOfChar.append(i)
                indexOfChar.append(k)
                return indexOfChar

def encryption(plainText, key,char1,char2):
    cipherText = []

    keyMatrix = generateKeyMatrix(key,char1,char2)

    i = 0
    while i < len(plainText):

        n1 = indexLocator(plainText[i], keyMatrix,char1,char2)
        n2 = indexLocator(plainText[i + 1], keyMatrix,char1,char2)

        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]

            i2 = (n2[0] + 1) % 5
            j2 = n2[1]

            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
            cipherText.append(", ")

        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] + 1) % 5

            i2 = n2[0]
            j2 = (n2[1] + 1) % 5

            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
            cipherText.append(", ")

        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            cipherText.append(keyMatrix[i1][j2])
            cipherText.append(keyMatrix[i2][j1])
            cipherText.append(", ")

        i += 2
    return cipherText

def main():

    key = input("Enter key: ").replace(" ", "").upper()
    uniteChar = input("묶음문자입력('/'로구분): ").replace("/", "").upper()
    plainText = input("Plain Text: ").replace(" ", "").upper()

    char1=uniteChar[0]
    char2=uniteChar[1]
    convertedPlainText = convertPlainTextToDiagraphs(plainText,char1,char2)

    cipherText = "".join(encryption(convertedPlainText, key, char1, char2))
    print(cipherText)

if __name__ == "__main__":
    main()



