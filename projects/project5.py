# PASSWORD GENRATOR::::
import random
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1",'2' ,'3' ,'4' , '5', '6', '7', '8', '9']
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '{', '}', '[', ']', '|',':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '\\', '`', '~']
print("Welcome To Password Generator")
nr_letter=int(input("enter no. oof letter u want in ur password\n"))
nr_number=int(input("enter no. u want in ur password\n"))
nr_symbols=int(input("enter no. of symbols u want in ur password\n"))

password=[]
for i in range(1,nr_letter+1):
    password.append(random.choice(alphabets))
   
for i in range(1,nr_number+1):
    password.append(random.choice(numbers))
    
for i in range(1,nr_letter+1):
    password.append(random.choice(symbols))
    
random.shuffle(password)
print(password)

final_password=""
for i in password:
    final_password += i
print(final_password)