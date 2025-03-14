
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
    
    print("")
    response1 = input("Would you like to encrypt or decrypt a word? (You must know the encryption key for both!)(Y/N) ").upper()

    if (response1 == "N"):
        cont = False
        break

    elif (response1 == "Y"):
        
        print("")
        response2 = input("Encrypt or Decrypt? (E/D) ").upper()

        if (response2 == "E"):

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

        
        elif (response2 == "D"):

            print("")
            encryption_key = int ( input("Enter an encryption key. ") )
            encrypted_text = ""

            caesar = create_dictionary(-encryption_key)

            print("")
            text = input("Enter your text to decrypt: ").upper()
            print(text)

            print("")

            for letter in text:
                
                if ( 'A' <= letter <= 'Z' ):
                    num = ord(letter)
                    encrypted_text += caesar[num - 65][chr(num)]
                
                else:
                    encrypted_text += letter

            print(encrypted_text)


    response3= input("Would you like to continue? (Y/N) ").upper()

    if (response3 == "N"):
        cont = False
        print("")
        print("Bye!")