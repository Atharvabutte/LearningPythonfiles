# this function open files or it takes two arguments & r is default argument
# Syntax = open('file name','operation on file')
# there are three basic operation i.e 1.r for reading 2.w for write 3.a for append 
# append is used for add the sentence in last without delteing previous data that particular file 
# f = open('random.txt','a')
# f.write("\nHey this is my  computer you want to buy this computer")
# #  This close function is used for close the file  
# f.close()

# Mydoc = open('newfile.jason','w')
# Mydoc.write('This is my first dictionary')
# Mydoc = open('newfile.jason','a')
# Mydoc.write('. I will write something in future')
# Mydoc = open('PrintATable.py','rb')
# text = Mydoc.read()
# print(text)


# Readlines function

# L = open('random.txt','r')
# # print(L.readline())
# i = 0
# while True:
#     i = i + 1
#     line = L.readline()
#     if not line:
#         break
#     Marks1 = line.split(",")[0]
#     Marks2 = line.split(",")[1]
#     Marks3 = line.split(",")[2]
#     print(f"Marks in Maths subject for Student {i} :{Marks1}")
#     print(f"Marks in English subject for Student {i} :{Marks2}")
#     print(f"Marks in Science subject for Student {i} :{Marks3}")
from os import close


L = open('random.txt','w')
lists = ["1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10"]
for list in lists:
    L.write( list +'\n')



