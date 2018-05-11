#Code cesar whit k=2
cipher_text = raw_input("Enter text: ").lower()
plain_text =''
# for i in cipher_text:
# 	if(i.isalpha()):

# 		dis = (ord(i) -ord('a')+2)%26
# 		plain_text += chr(ord('a')+dis)
# 	else:
# 		plain_text += i
# print "\nYour plain text:\n"+ plain_text


#Cach 2 dung makestrane
import string 
table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print "\nYour string: "
print cipher_text.translate(table)