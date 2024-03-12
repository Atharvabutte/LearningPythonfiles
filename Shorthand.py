A = 185
B = 185
print("A is great no") if A>B else print("A is equal to B") if A==B else print("B is great no")


# Enumerate


Marks = [1,23,6,5,89,54,6,5,3,2,83]
for i , marks in enumerate(range(len(Marks))):
    print(i,Marks[i])
    if (Marks[i]== 89):
        exit()
        
    
