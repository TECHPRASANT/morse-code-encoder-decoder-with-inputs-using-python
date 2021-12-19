# morse code encoder/decoder with inputs
## Overview
Morse code is a character encoding scheme used in telecommunications. It is named after the inventor of the telegraph Samuel Morse and represents textual characters as combinations of long (dashes) and short (dots) electronic pulses, lights or sounds. <p>For example, the letter J is coded as .---, ! as -.-.-- and 1 as .−−−− A single space is used to separate characters within a word and 3 spaces between words. Morse is case-insensitive, so capital letters are used as a matter of course.</p> <p>For example, the message HELLO WORLD in Morse code is: .... . .-.. .-.. --- .-- --- .-. .-.. -..</p> In addition to letters, digits and punctuation, there are some special service codes, the most notorious of which is the international distress signal SOS, coded as ...−−−... These special codes are treated as single characters, but transmitted as separate words.#
## Program code:
```python
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
```
## Output of the program
<b>Welcome to Wolmorse <br>
This program encodes and decodes Morse code.<br>
  Would you like to encode (e) or decode (d): g <br>
Invalid Mode<br>
Would you like to encode (e) or decode (d): d<br>
What message would you like to decode: .... . .-.. .-.. --- .-- --- .-. .-.. -..<br>
HELLO WORLD<br>
Would you like to encode/decode another message? (y/n): a<br>
Would you like to encode/decode another message? (y/n): y<br>
Would you like to encode (e) or decode (d): e<br>
What message would you like to encode: Hello WORld<br>
.... . .-.. .-.. --- .-- --- .-. .-.. -..<BR>
Would you like to encode/decode another message? (y/n): n<br>
Thanks for using the program, goodbye!
## Thankyou.
