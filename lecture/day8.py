# Functions with inputs

# def greeting(name):
#     print(f"Hello {name}")
#     print(f"how r u {name}")
# greeting("Aashna")

# # here name is parameter and value that is aashna is an argument here

# ---------------

# QUES:
'''
Life in Weeks
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.Where x is replaced with the actual calculated number of weeks the input age has left until age 90.


Example Input:56

Example Output:You have 1768 weeks left.
'''

# sol:
# def life_in_weeks(age):
#     age_in_weeks=(90-age)*52
#     print(f"You have {age_in_weeks} weeks left.")
# life_in_weeks(56)

# ---------------------

# FUNCTION WITH MORE THAN 1 INPUT:

# def greet(name,location):
#     print(f"hello my name is {name} and im born in {location}")
# greet("Aashna", "Karnal")

# ----------

# POSITIONAL ARGUMENTS

# def abc(a,b,c):
#     print(f"hey {a}, b is {b}, c is {c}")
# # abc(12,"aadj",34)

# # KEYWORD ARGUMENT:
# abc(b=32,c="das",a=23)

# ---------------------

# QUES:Love Calculator
'''
 This is a difficult challenge!  

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 
e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 

Love Score = 53

Example Input 
calculate_love_score("Kanye West", "Kim Kardashian")
Example Output:42

'''

# sol:
# def calculate_love_score(name1,name2):
#     name=(name1+name2).lower()
#     true_count=sum(name.count(i)for i in "true")
#     love_count=sum(name.count(i)for i in "love")
#     love_score=str(true_count)+str(love_count)
#     print(love_score)
 

# ------------------------------------------------