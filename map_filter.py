# Map
# Marks = [45,18,93,88,7,1,58,67,48,60,80,99,100]

# def Passing_criteria(Marks):
#     if Marks >= 90:
#         return 'A'
#     elif 80 <= Marks < 90:
#         return 'B'
#     elif 70 <= Marks < 80:
#         return 'C'
#     elif 60 <= Marks < 70:
#         return 'D'
#     else:
#         return 'FALL'
    

# Grades = map(Passing_criteria, Marks)
# print(f"Exam scores: {Marks}")

# print(list(Grades))


#   FILLTER
# Marks = [77,67,84,35,55]
# def Fail_students(score):
#     return score < 55
   
# Result = filter(Fail_students, Marks)
# print(list(Result))


# ANOTHER EXAMPLE

Name = ["Atharva","Roshan","tanush","Sachin", "vbemmcn", "heebwbsinnen"]

# a = map(lambda x : x.startswith("A"),Name)
# a = map(lambda x : x.endswith("n"),Name)
# print(list(a))

a = map(lambda x : x.lower(),Name)
print(list(a))