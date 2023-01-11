#Question 4- morse code tranlator
morse_dictionary={'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def string_to_morse( message):
    morse=''
    for i in message :
         if i==' ':
            morse+=' '      #adding space in case the string has space
         else:
            morse=morse+morse_dictionary[i]+' '     #updating the string after extracting its morse code from the dictionary
    
    return (morse)
def morse_to_string(code):      
    
    word=''     #To store each word one by one 
    sentence='' #To store the encoded string
    code+=' '
    c=0
    for i in code:
         if (i != ' '):
            c = 0           #counting space
            word += i       #making the word letter by letter
         else:
            c += 1
            if c == 2 :     # two spaces means new word
                sentence += ' ' # adding space in sentence
            else:
                sentence += list(morse_dictionary.keys())[list(morse_dictionary.values()).index(word)] #updating the sentence with morse code that is doin by extracting the index 
                word = ''
    print(sentence)
    return sentence
def main():
    message=input("\nEnter the string to be converted to morse code ")
    print("\nThe encoded message is ",string_to_morse(message.upper()))     #just in case the user didnt write in upper case
    code=input("\nEnter the code to be decoded ")
    print("\nThe decoded message is ",morse_to_string(code))    #to encode

if __name__ == '__main__':
	main()