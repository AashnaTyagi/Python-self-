# FUNCTIONS

# 1)built in function: len, range, print etc
# 2)defining func
 
# def myFunc():
#     print("hello")
#     print("bye")
# myFunc()

# ---------------

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# --------------

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# SOL:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def cycle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for i in range(1,7):
#     cycle()

# --------------------

# WHILE LOOP:

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Sol:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def cycle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while at_goal()!= True:
#     cycle()

# ----------------------

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def cycle():
    
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while at_goal()!= True:
#     if wall_in_front():
#         cycle()
#     else:
#         move()

# -----------------------------

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# SOL

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def cycle():
#     turn_left()
#     while wall_on_right():
#         move()

#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while at_goal()!= True:
#     if wall_in_front():
#         cycle()
#     else:
#         move()

# --------------------

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# SOL:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def cycle():
#     pass
# while at_goal()!= True:
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()