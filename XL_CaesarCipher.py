#Xinyu Lin
#Computer Science Period 4 - Ms.Lerohl
#Caesar Cipher Project
#1/15/15

message = raw_input ("Enter a message to be encrypted or decrypted")                #raw_input prompts the user to enter a message to be encrypted or decrypted
evenShift = int(raw_input ("Enter an integer between 1 and 94 for even shift"))     #raw_input prompts the user to enter an integer for even shift
oddShift = int(raw_input ("Enter an integer between 1 and 94 for odd shift"))       #raw_input prompts the user to enter an integer for odd shift

while evenShift >94 or evenShift <1:                                                                        #the while loop sets the input validation for even shift
    print "Your even-shift value is not within the range. Please enter another number between 1 and 94"     #if the evenShift is >94 or <1; it will print that the input is not within the range
    evenShift = int(raw_input ("Enter an integer between 1 and 94 for even shift"))                         #the user is prompted to enter another number between 1 and 94.
                                                                                                            #the while statement keeps asking users to enter an interger until the integer in within the range

while oddShift >94 or oddShift <1:                                                                          #the while loop sets the input validation for odd shift
    print "Your odd-shift value is not within the range. Please enter another number between 1 and 94"      #if the oddShift is >94 or <1; it will print that the input is not within the range
    oddShift = int(raw_input ("Enter an integer between 1 and 94 for odd shift"))                           #the user is prompted to enter another number between 1 and 94.
                                                                                                            #the while statement keeps asking users to enter an interger until the integer in within the range
    
def encrypt(message, evenShift, oddShift):          #the encryt function is defined with parameters from user-input: message, evenShift, and oddShift
    encrypted = ""                                  #variable encrypted is set to an empty string
    count = 0                                       #the count variable is set to integer 0
    for char in message:                            #a loop is used. The loop-variable "char" holds one character from the string-variable "message" at a time
        if count%2==0:                              #even-shift: if the index of the character is even
                numChar=ord(char)                   #ord function converts the character into its Ascii value
                numChar=numChar + evenShift         #even shift takes place--> adding the character's Ascii value to the evenShift
                if numChar > 126:                   #if numChar is greater than 126
                    numChar= numChar-95             #the result is substracted by 95 because the range of the Ascii value is from 32 to 126
                elif numChar < 32:                  #if numChar is less than 32
                    numChar= numChar+95             #the result is added by 95 because the range of the Ascii value is from 32 to 126
                shiftChar= chr(numChar)             #chr function converts the Ascii value to the shifted character 
                encrypted= encrypted + shiftChar    #this added the shifted character to the empty string so that the results would be printed horizontally 
                count=count+1                       #after the loop, count is added by 1 to move onto the next character
        elif count%2==1:                            #odd-shift: if the index of the character is odd
                numChar= ord(char)                  #ord function converts the character into its Ascii value
                numChar= numChar + oddShift         #odd shift takes place--> adding the character's Ascii value to the oddShift
                if numChar > 126:                   #if numChar is greater than 126
                    numChar= numChar-95             #the result is substracted by 95 because the range of the Ascii value is from 32 to 126
                elif numChar < 32:                  #if the result is less than 32
                    numChar= numChar+95             #the result is added by 95 because the range of the Ascii value is from 32 to 126
                shiftChar= chr(numChar)             #chr function converts the Ascii value to the shifted character 
                encrypted= encrypted + shiftChar    #this added the shifted character to the empty string so that the results would be printed horizontally 
                count=count+1                       #after the loop, count is added by 1 to move onto the next character
    return encrypted                                #the result of the function is returned 

def decrypt(encryptedMessage,evenShift,oddShift):   #the decrypt function is defined with parameters: encrytedMessage, evenShift, and oddShift
    count=0                                         #the count variable is set to zero
    decrypted=""                                    #decrypted varaible is set to an empty string 
    for char in encryptedMessage:                   #a loop is used. The loop-variable "char" hold one character from the string-variable "message" at a time 
        numChar=ord(char)                           #the ord function assigns the Ascii value of the character to the variable, numChar
        if count%2==0:                              #even-shift: if the index is even
            numChar=numChar-evenShift               #the value of evenShift is subtracted from numChar to decrypt the message
            if numChar<32:                          #if the difference is less than 32, it means that during decrypt, 95 was substracted from the sum of numChar and evenShift to make the value within the range of 32 and 126
                numChar=numChar+95                  #the difference is added by 95 to make the value between the range of 32 to 126
        else:                                       #else conditional statement for oddshift
            numChar=numChar-oddShift                #oddShift is subtracted from the Ascii value of the character to decrypt the message
            if numChar<32:                          #if the difference is less than 32, it means that during decrypt, 95 was substracted from the sum of numChar and evenShift to make the value within the range of 32 and 126
                numChar=numChar+95                  #the difference is added by 95 to make the value between the range of 32 to 126
        shiftChar=chr(numChar)                      #chr function converts the Ascii value to a character; the character is assinged to shiftChar
        decrypted=decrypted+shiftChar               #shiftChar is added to an empty string defined earlier to print out the results horizontally 
        count=count+1                               #after the loop, count is added by 1 to move onto the next character 
    return decrypted                                #the function returns a result

def CaesarCipher():                                                         #a main function, CasesarCipher, is defined. This function starts the program and combines encryption and decryption
    action=raw_input(str("Do you want to encrypt or decrypt the message?")) #the user-input prompts the user to either encrypt or decrypt the message
    if action == ("encrypt"):                                              #if the user wants to encrypt
        print ("Your original message is "+message)                        #prints out the original message
        encryptedMessage=encrypt(message, evenShift, oddShift)             #calls the encrypt function and sets the outcome to "encryptedMessage"
        print ("Your encrypted message is " + encryptedMessage)            #prints out the encrypted message 
    elif action == ("decrypt"):                                            #if the user wants to decrypt
        print ("Your original message is "+message)                        #prints out the original message
        decryptedMessage=decrypt(message,evenShift,oddShift)               #calls the decrypt function and sets the outcome to "decryptedMessage"
        print ("Your decrypted message is " + decryptedMessage)            #prints out the decrypted message 
    else:                                                                  
        while action!=("encrypt") and action!=("decrypt"):                          #input-validation for action. If the action is not encrypt or decrypt
            print ("Wrong input")                                                   #"Wrong input" is printed
            action=raw_input(str("Do you want to encrypt or decrypt the message?")) #while the action does not equal to encrypt or decrypt, the input validation ask the user to input the right action
            if action == ("encrypt"):                                               #if the new action entered is encrypt
                print ("Your original message is "+message)                         #prints out the original message
                encryptedMessage=encrypt(message, evenShift, oddShift)              #calls the encrypt function and sets the outcome to "encryptedMessage"
                print ("Your encrypted message is " + encryptedMessage)             #prints out the encrypte message
            elif action == ("decrypt"):                                             #if the new action entered is decrypt
                print ("Your original message is "+message)                         #prints out the original message
                decryptedMessage=decrypt(message,evenShift,oddShift)                #calls the decrypt function and sets the outcome to "decryptedMessage"
                print ("Your decrypted message is " + decryptedMessage)             #prints out the decrypted message 

CaesarCipher()           #the main function is called; allowing the program to be run 


    
