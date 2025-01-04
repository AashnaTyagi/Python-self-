# conditional statements (if / else)--->

# #syntax:

# if condition:
#     do this
# else:
#     do this

# # eg 1-
# water_level=50
# if water_level>=50:
#     print("drain water")
# else:
#     print("let it flow")

# ----------------------------

# use draw.io for flowcharts nd diagrams

# ----------------------------

# # eg2-
# print("welcome to rollcoster")
# height=int(input("pls enter height: "))
# if height>=120:
#     print("u may enter the ride")
# else:
#     print("grow up kiddo")

# ----------------------------

# comparison operators--->

# > greater than
# < lesser than
# >=  greater than equal to
# <= lesser than equal to
# = assigning value
# == comparing value

# ----------------------------

# modulo operator(%)-->
# gives us remainder

# print(10%2)        #completely divides
# print(10%3)        #gives remainder 1

# even no. : if 12%2==0 if output = 0 then the no. is even if it is not equal to 0 then it is a odd no.

# eg:
# no_to_check=int(input("no u want to check: "))
# if no_to_check % 2 == 0:
#     print("even")
# else:
#     print("odd")
    
# ----------------------------

# Nested if/else-->

# #syntax:

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

## eg 1: for height nd age 18 above pay 20 , under 18 pay 7
# print("welcome to rollcoster")
# height=int(input("pls enter height: "))
# if height>=120:
#     print("u may enter the ride")
#     age=int(input("pls enter age "))
#     if age<=18:
#         print("pay $7")
#     else:
#         print("pay $12")
# else:
    # print("grow up kiddo")

# ----------------------------

# elif condition:---> only A,B, C wil be carried out (any one condition takes place)

# syntax:
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do this


# eg 1: for height nd age less than 12 year pay 5, 12 to 18 pay 7,more than 18 year pay 12

# # sol:
# print("welcome to rollcoster")
# height=int(input("pls enter height: "))
# if height>=120:
#     print("u may enter the ride")
#     age=int(input("pls enter age "))
#     if age<=12:
#         print("pay $5")
#     elif age<=18:
#         print("pay $7")
#         # can add as manya elif as u want
#     else:
#         print("pay $12")
# else:
#     print("grow up kiddo")


# ----------------------------

# exercise:

# # que:BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

# sol:

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)
# if bmi<18.5:
#     print("underweight")
# elif 18.5<=bmi<25:
#     print("normal weight")
# else:
#     print("over weight")
# ----------------------------

# MULTIPLE IF CONDITIONS---> if condition A is true then it will check nd go to B nd if it is true then to C 

# Syntax:
# if condition 1:
#    do A
# if condition 2:
#    do B
# if condition C:
#    do C

# eg:
# # sol:
# print("welcome to rollcoster")
# height=int(input("pls enter height: "))
# bill=0

# if height>=120:
#     print("u may enter the ride")
#     age=int(input("pls enter age "))

#     if age<=12:
#         bill=5
#         print("pay $5")
#     elif age<=18:
#         bill=7
#         print("pay $7")
#         # can add as manya elif as u want
#     else:
#         bill=12
#         print("pay $12")

#     # could be at same indentation level as if elif 
#     photo=input("want pic yes or no? ")
#     if photo=="yes":
#         bill+=3
#         # bill=bill+3
#     print(f"final bill is {bill} ")

# else:
#     print("grow up kiddo")
# ----------------------------

# # exercise:

# # sol:
# print("welcome to python pizza deliveries!")
# size=input("wht size u want? S, M , L: ")
# pepporini=input("do u want pepporini or not? Y or N: ")
# extra_cheese=input("want cheese? Y or N: ")
# bill=0
# if size =="S":
#     bill+=15
    
# elif size=="M":
#     bill+=20
# elif size=="L":
#     bill+=25
# else:
#     print("u typed wrong input")

# if pepporini=="Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3

# if extra_cheese=="Y":
#     bill+=1
# print(f"final bill is : {bill}")

# ----------------------------

# logical operators

# and,or, not

# and: returns true if both are true 
# or: requires one statement to be true to return true
# not: returns reversed value suppose ans is true then it returns false

# que:
# sol:
# print("welcome to rollcoster")
# height=int(input("pls enter height: "))
# bill=0

# if height>=120:
#     print("u may enter the ride")
#     age=int(input("pls enter age "))

#     if age<=12:
#         bill=5
#         print("pay $5")
#     elif age<=18:
#         bill=7
#         print("pay $7")
#         # can add as manya elif as u want
#     elif age>=45 and age<=55:
#     # elif 45<= age <=55:
#         print("everything is going to be ok. have a free ride on us")
#     else:
#         bill=12
#         print("pay $12")

#     # could be at same indentation level as if elif 
#     photo=input("want pic yes or no? ")
#     if photo=="yes":
#         bill+=3
#         # bill=bill+3
#     print(f"final bill is {bill} ")

# else:
#     print("grow up kiddo")
# ----------------

# que:

# a = 5
# b = 7
 
# if a >= b and a != b:
#     print("A")
# elif not a >= b and a != b:
#     print("B")
# else:
#     print("C")

# ----------------------------