# with open('newfile.txt', 'w') as fl:
#     fl.write("Atharva")
with open('newfile.txt', 'a') as fl:
    fl.write("Hey this is my first program on IO function")
with open('newfile.txt', 'r') as fl:
    text = fl.read()
    print(text)
# with open('newfile.txt', 'r') as fl:
#     fl.seek(15)
#     text = fl.read()
#     print(text)  
# with open('newfile.txt', 'w') as fl:
#     fl.truncate(128)
# with open('newfile.txt', 'r') as fl:
#     text = fl.read()
#     print(text)
    
  

