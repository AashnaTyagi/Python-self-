# DICTIONARy ND NESTING::

# dict={"key":"value","key2":"value"}
# print(dict["key"])
# # adding
# dict["key3"]="value3"
# # removing item
# dict={}
# print(dict)
# # loops
# for key in dict:
#     print(key)
#     print(dict[key])  #give value as well

# -----------------------------------------------------------

# QUES:

# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 
# The final version of the student_grades dictionary will be checked. 

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 
# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

# ANS:

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades = {}

# for student, score in student_scores.items():

#     if score >= 91:
#         grade = "Outstanding"
#     elif score >= 81:
#         grade = "Exceeds Expectations"
#     elif score >= 71:
#         grade = "Acceptable"
#     else:
#         grade = "Fail"
    
#     student_grades[student] = grade

# print(student_grades)

# ----------------------------------------------

# NESTING LIST ND DICT

# capital={
#     "france":"paris",
#     "germany":"berlin",
# }
# travel_log={
#     "france":["paris","lille","dijon"],
#     "germany":["stuttgart","berlin"]
# }
# print(travel_log["france"][1])
# # lille

# ------------

# nested_list=["a","b",["c","d"]]
# print(nested_list[2][1])
# # prints "d"

# ---------------

# travel_log={
#     "france":{
#     "mo._of_time_visited":8,   #dict form
#     "city_visited": ["paris","lille","dijon"]},

#     "germany":{
#        "city_visited": ["hamburg","stuttgart","berlin"],
#        "no._of_time_visited":5,
#         }
# }
# print(travel_log["germany"]["city_visited"][2])
# # berlin

# ----------------------------------------------

