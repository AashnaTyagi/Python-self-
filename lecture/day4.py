# RANDOM MODULE

# import random
# a=random.randint(4,9)    #works for integer only
# print(a)

# ------------

# import random
# random_no=random.random()     #creates random no. btwn 0 to 1 only
# print(random_no)

# OR

# import random
# random_no=random.random()*10     #expands random no.'s range 
# print(random_no)

# ------------

# import random
# a=random.uniform(1,10)    #works for float including both 1,10
# print(a)

# ------------

# import random
# a=random.randint(0,1)    #works for integer only
# if a==0:
#     print("HEADS")
# else:
#     print("TAILS")

# ---------------------------------------------------------------

# LISTS: sq brackets[ ]

# states=["haryana","punjab","xhfchg","trcyj"]
# states[2]="J and K"
# print(states)
# print(states[3])
# print(states[-1])   #total length -1 here 4-1 that is 3 

# ------------

# FUNCTIONS ON LISTS:

# states=["haryana","punjab","xhfchg","trcyj"]
# states.append("J and K")
# print(states)   
# # ['haryana', 'punjab', 'xhfchg', 'trcyj', 'J and K']

# -----------

# states=["haryana","punjab","xhfchg","trcyj"]
# states.remove("xhfchg")
# print(states)  
# # ['haryana', 'punjab', 'trcyj']

# -----------

# states=["haryana","punjab","xhfchg","trcyj"]
# states.extend(["J and K","uvfj","wsedfvgub"])
# print(states) 

# -----------

# list.insert(a,b)=====>>>>> insert item at given position a ki position p b ajega 

# list.pop([2])=====>>>>> delets the 2nd index item 

# list.pop()=====>>>>> delets the last item of list if no index is specified

# list.clear()=====>>>>> del all item of list

# list.count(a)=====>>>>> counts the repeatation of a in list

# list.sort(reverse=True)=====>>>>> reverses the list

# ---------------------------------------------

# PICKING RANDOM ITEM FROM THE LIST:

# import random
# friends=["alice","bob","david","charlie",'nhjyug']

# # first way
# print(random.choice(friends))

# # 2nd way by index
# random_index=random.randint(0,4)
# print(friends[random_index])

# ------------------------------------------------------

# fruits=["banana","mango","apple","grapes"]
# veg=["spinach","potatos","tomatos","brinjal"]
# total=[fruits,veg]
# print(total)

# -------

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])

# ------------------------------------------------------