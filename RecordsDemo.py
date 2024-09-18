
def create_dictionary( en_key ):
    caesar = []
    
    x = 0
    y = 0
    
    for lp in range (0, 26, 1):
        x = 65 + lp
        y = 65 + lp + en_key

        if (y < 91):
            letter = { chr(x) : chr(y)}
        
        else:
            letter = { chr(x) : chr(y - 26)}
        
        caesar.append(letter)
    
    return(caesar)

cont = True

while (cont):
    response1 = input("Would you like to encrypt or decrypt a word? (You must know the encryption key for both!)(Y/N) ")
    
    print("")
    encryption_key = int ( input("Enter an encryption key. ") )
    encrypted_text = ""

    caesar = create_dictionary(encryption_key)

    print("")
    text = input("Enter your text to encrypt: ").upper()
    print(text)

    print("")

    for letter in text:
        
        if ( 'A' <= letter <= 'Z' ):
            num = ord(letter)
            encrypted_text += caesar[num - 65][chr(num)]
        
        else:
            encrypted_text += letter

    print(encrypted_text)

    response1 = input("Would you like to continue? (Y/N) ").upper()

    if (response1 == "N"):
        cont = False
        print("")
        print("Bye!")