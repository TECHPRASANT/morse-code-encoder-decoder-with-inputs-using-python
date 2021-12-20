# Coding Challenge 2
# Name:
# Student No:

#A morse code encoder/decoder

# A Morse code in tuple
MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)
# Converting tuple to dictionary
dictionary = dict((i, j) for j, i in MORSE_CODE)

# This function is used to print intro
def print_intro():
    print("Welcome to the morse \nThis program encodes and decodes Morse code.")
    return 0

# This function is used to get all inputs
def get_input():
    check = input("Would you like to encode (e) or decode (d) : ")
    if check!='e' and check!='d' :
        #if user doesn't choose e or d in above input , it prompts Invalid mode.
        print("Invalid mode")
    elif check=='e'or check=='E':
        #if user choose small e or capital E, then it runs encode mode. 
        en_message=str(input("What message would you like to encode:")).upper() #accept english text
        encrypt_output= encode(en_message.upper()) #it converts inputed english text to morse code
        print (encrypt_output) #prints encripted output
    elif check=='d'or check=='D':
        #if user choose small d or capital D, then it runs decode mode. 
        de_message=input("What message would you like to decode:") #accept morse code
        decrypt_output = decode(de_message) #it converts inputed morse code to english text
        print (decrypt_output) #prits decrypted output

#This function continue program till user type n
def get_continue():
    another=str(input("Would you like to encode/decode another message? (y/n):"))
    while another=='y':
        # get_input() and get_continue() functions continue when user type y when above input prompt up.
        get_input() 
        get_continue()
        break
    if another=='y' or another!='y' and another!='n':
        #if user type y get continue funtion runs. or if user type others letter(not y and n) again get continue funtion runs.
        get_continue()   
    if another=='n':
        #program ends when user type n
        print("Thanks for using the program, goodbye!")
        quit() #program ends

# This function is used to encrypt
# English to  morse code                     
def encode(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += dictionary[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher.strip()


# This function is used to decrypt
# Morse code to Englishdef decrypt(message):
def decode(message):
    message += ' '
    decipher = ''
    code_text = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            code_text += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(dictionary.keys())[list(dictionary
                .values()).index(code_text)]
                code_text = ''
 
    return decipher
    
#main funtion
def main():
    print_intro() #this funtion executes in first
    get_input()  #this funtion executes in second
    get_continue()  #this funtion executes in third


#program begins from here
if __name__ == '__main__':
    main() #executes main funtion
