
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt_caesar(caeser_str,offset):

	new_caeser_str = ""

	for char in caeser_str:
		if(char.lower() in alphabet):
			
			if(offset + alphabet.index(char.lower()) >= 26):
				wraparound = offset + alphabet.index(char.lower()) - 26
				#print(wraparound)
				#print("over")
				if(ord(char) >= 0x61): # lower case
					new_char = chr(0x61 + wraparound)
				else: # upper case
					new_char = chr(0x41 + wraparound)
				new_caeser_str += new_char
			else:
				new_char = chr(ord(char) + offset)
				new_caeser_str += new_char
			
		else:
			# non alphabetic characters just remain as is.
			new_caeser_str += char
			
	return(new_caeser_str)

def main():

	inputed = True
	while(inputed):
		try:
			offset = int(input("Please enter the offset:\n>")) % 26
			inputed = False
		except:
			print("Needs to be an integer.")
			inputed = True
			
	print("Simplifying the offset as %d." % offset)
	print("The cipher looks like:\n\n%s\n%s\n"% (alphabet,encrypt_caesar(alphabet,offset)) )
	
	caeser_str = ""
	while(not caeser_str):
		caeser_str = input("Please enter string to be modified\n>")

	encrypted = encrypt_caesar(caeser_str,offset)
	print("The encrypted text:\n%s" % encrypted)

if __name__ == "__main__":
	main()
