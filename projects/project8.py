# CAESSAR CIPHER:
print("-------------------------------------------")
print("--------WELCOME TO CAESAR CIPHER-----------")
print("-------------------------------------------")

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n")
shift=int(input("Type the shift number:\n"))

# # hello 2
# def encrypt(original_text,shift_amount):
#     cipher_text=""    #creat empty strg    #j
#     for letter in original_text:
#         shifted_position=alphabets.index(letter)+shift_amount    #7-->9
#         shifted_position%=len(alphabets)   #so that range stays btwn 0-25
#         cipher_text+=alphabets[shifted_position]   #j
#     print(f"Here is encoded result: {cipher_text}")
# encrypt(text,shift)

# def decrypt(original_text,shift_amount):
#     output_text=""    #creat empty strg    #j
#     for letter in original_text:
#         shifted_position=alphabets.index(letter)-shift_amount    #7-->5
#         shifted_position%=len(alphabets)   #so that range stays btwn 0-25
#         output_text+=alphabets[shifted_position]   #j
#     print(f"Here is decoded result: {output_text}")
# decrypt(text,shift)

def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""    #creat empty strg  

    # took this part out of for loop bcoz when encode ab gives cd but when decode cd gives af so to change that take it out of for loop now decode wont give any error
    
    if encode_or_decode=="decode":
        shift_amount*=-1 
    for letter in original_text:
        if letter not in alphabets:
            output_text+=letter
        else:
            # if encode_or_decode=="encode":
            #     shift_amount*=1

            shifted_position=alphabets.index(letter)+shift_amount    
            shifted_position%=len(alphabets)   #so that range stays btwn 0-25
            output_text+=alphabets[shifted_position]
            print(f"Here is {encode_or_decode}d result: {output_text}")

should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n")
    shift=int(input("Type the shift number:\n"))


    caesar(text,shift,direction)
    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart==False:
        print("GoodBye")