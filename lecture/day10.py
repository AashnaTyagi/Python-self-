# FUNCTIONS:

# def myFunc():
#     # do here 

# /-------------------

# FUNC WITH OUTPUTS:

# def format_name(f_name,l_name):

# # convert string to title
#     print(f_name.title())
#     print(l_name.title())
#     # return f"{f_name} {l_name}"
# format_name("aashna","TYaGI")
'''Aashna
Tyagi'''

# ---------------------------------

# def func1(text):
#     return text + text

# def func2(text):
#     return text.title()

# # output=func1("hello")
# # print(output)
# # # hellohello

# output=func2(func1("hello"))
# print(output)
# # Hellohello

# ---------------------------------

# MULTIPLE RETURN VALUES:

# def format_name(f_name,l_name):
#     # if f_name=="" or l_name=="":
#     #     return "no value entered"
    
#     formated_f_name= f_name.title()
#     formated_l_name= l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#     print("this line doesnt get executed bcoz its printed after return statement")

# print(format_name("AaSHna","tYagi"))
# # Aashna Tyagi

# # print(format_name(input("wht is ur name?: "),input("wht is ur surname?: ")))
# # gives error

# ---------------------------------

# QUES:

# SOL:
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# ---------------------------------

# DOCSTRINGS:
# u can use doc string to multiline comments that doc ur code
"""this 3 
are 
docstring"""

# ---------------------------------