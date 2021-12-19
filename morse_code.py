# Name: Prashant Bhandari

# A Morse code encoder/decoder
# Dictionary representing the morse code chart
MORSE_CODE = {
## Letters
'A': '.-','B': '-...','C': '-.-.',
'D': '-..','E': '.','F': '..-.','G': '--.',
'H': '....','I': '..','J': '.---','K': '-.-',
'L': '.-..','M': '--','N': '-.','O': '---','P': '.--.',
'Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-',
'V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..',
## Numbers
'0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....',
'6': '-....','7': '--...','8': '---..','9': '----.',
## Punctuation
'(': '-.--.',')': '-.--.-','-': '-....-','_': '..--.-',
'.': '.-.-.-',',': '--..--',':': '---...',';': '-.-.-.',
'=': '-...-','?': '..--..','!': '-.-.--',"'": '.----.',
'"': '.-..-.','@': '.--.-.','&': '.-...','$': '...-..-',
'x': '-..-','/': '--..-.'
}

#make reverse morse code dictionary
reverse_dict = {
	MORSE_CODE[key] : key for key in MORSE_CODE
}


# This function is used to print intro
def print_intro():
    print("Welcome to the morse \nThis program encodes and decodes Morse code.")
    return 0


# This function is used to get all inputs
def get_input():
    check = input("Would you like to encode (e) or decode (d) : ")
    if check!='e' and check!='d' :
        print("Invalid mode")
    elif check=='e'or check=='E':
        en_message=str(input("What message would you like to encode:")).upper()
        encrypt_output= encrypt(en_message.upper())
        print (encrypt_output)
    elif check=='d'or check=='D':
        de_message=input("What message would you like to decode:")
        decrypt_output = decrypt(de_message)
        print (decrypt_output)

#This function continue program till user type n
def get_continue():
    another=str(input("Would you like to encode/decode another message? (y/n):"))
    while another=='y':
        get_input()
        get_continue()
        break
    if another=='n':
        print("Thanks for using the program, goodbye!")
                     
# This function is used to encrypt
# English to  morse code  
def encrypt(message):
	result = ''
	for ch in message.upper():
		result += MORSE_CODE.get(ch, ch)
		result += ' '
	return result.strip()

# This function is used to decrypt
# Morse code to English
def decrypt(message):
	result = ''
	for ch in message.split():
		result += reverse_dict.get(ch, ch)
	return result

#main function
def main():
    print_intro()
    get_input() 
    get_continue()   

#Executes the main function
if __name__ == '__main__':
    main()
    
