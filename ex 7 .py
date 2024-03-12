import os 

files = os.listdir()
print(files)


for file in files:
    if file.endswith(".txt"):
        print(file)
        os.rename(f"{file}",f"{file.split(".")[0]}.md")