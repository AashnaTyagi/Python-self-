# Data type---->

# print("hello"[4])
# print("hello"[-2])

# # string
# print("123"+"456")    #concatenation

# # integer=whole no.
# print(123+456)

# large integer
# print(123,456)---> not allowed
# print(123_456)

# # float
# print(3.14)

# # boolean
# print(True)
# print(False)
# ---------------------

# type error,checking, coversion

# type error--->
# len("hello")

# # type chcking--->
# print(type("hello"))
# print(type(123))
# print(type(4.53))
# print(type(True))

# type coversion/casting--->
# print("123"+"234")   #concatenation
# print(int("123")+int("456"))
# print(int("123")+float("456"))


# # prob: print("6"+len(input("enetr your name")))   #shows error (cant be converted)
# # sol:
# name=input("enter name: ")
# length=len(name)
# print(type("no of letter in name: "))   #str
# print(type(length))   #int

# print("no of letter in ur name: " + str(length))
# # print(int("abc")+int("456"))  #error (cant be coverted)

# ---------------------

# # MATHEMATICAL OPERATION-->

# print("addition: ", 123+321)
# print(7-5)
# print(3*4)
# print(6/3)   # gives in float(called implicite type casting)
# print(6//3)  #int


# print(5/3)   #ans: 1.666666
# print(5//3)     #ans: 1
# print(2**2)    #power 

# order rule: P(), E**, M*,/ D, A+,S-
# print(3*3+3/3-3)


# ---------------------

# exercise : BMI calculator--->

# que: BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

# # sol:
# height = 1.65 
# weight = 84

# # Calculate the bmi using weight and height.
# bmi =weight/(height**2)

# print(bmi)
# print(int(bmi))

# ---------------------

# Number Manipulation--->
 
# 1)roundding off
# bmi =80/(1.65**2)
# print(bmi)
# print(round(bmi))
# print(round(bmi, 2))   #round of the no upto 2 decimal places

# 2)assignment operators(+=, -=,*=,/=)
# score=5
# score+=1
# print(score)

# 3)f-String
# score=5
# height= 1.8
# is_winning=True
# print("your score is "+ str(score)+ ", your height is "+str(height))
# # orrrrrrrrrrrr
# print(f"your score is = {score}, ur height is {height}, ur r winning {is_winning}")

# ---------------------
# que: What is the data type of the result of the variable a in the following line of code:
# a = int("5") / int(2.7)

# sol:int("5") is 5, int(2.7) is 2, so the code becomes: a = 5 ÷ 2 which equals 2.5, which is a float

# ---------------------