#Question 2
def isPalindrome(string):           #To check whether the given string(substring) is palindrome or not 
    if(string == string[::-1]):
        return True
    else:
        return False
def palin_by_removing_char(string) : #To see the character that need to be removed
	lb = 0
	ub = len(string) - 1
	while lb < ub:
		if string[lb] == string[ub]:    #to see if the string is palin 
			lb += 1
			ub -= 1
		else:
            
			if isPalindrome(string[lb + 1: ub+1]):      # substring sent to isPalin to check 
				return lb
			if isPalindrome(string[lb: ub]):
				return ub
			return 0            #If the string cant be converted tp palin
	return -1           #If the string is already palindrome
def main():
    string = input("Enter a string ")
    pos = palin_by_removing_char(string.lower())        # To store index of the position at which the character is to be removed, converting to lower case to avoid any error
    if pos == 0:
        print("Not possible")
    elif pos== -1:
        print("Possible without removing any character")
    else:
        print("It is possible to make the string palindrome by removing the character  ", string[pos])
        ch=string[pos]
        print("The new string is ",string.replace(ch, ''))
        
if __name__ == '__main__':
	main()