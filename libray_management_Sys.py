class Library:
    def __init__(self):
        self.Booklist = ["Rich dad poor dad", "Chemistry book", "C language", "Java Language"]
        self.No_of_books = len(self.Booklist)

    def Add_books(self):
        self.Addbooks = input("Enter books name: ")
        self.Booklist.append(self.Addbooks)
        self.No_of_books += 1
        return self.Booklist

    def Display_available_Books(self):
        print(f"Available books: {self.Booklist}")

    def NoOfBooks(self):
        print(f"No of books: {self.No_of_books}")

Lib = Library()
print(Lib.Booklist)
print(f"No of books:{Lib.No_of_books}")
Lib.Add_books()
Lib.Display_available_Books()
Lib.NoOfBooks()



#  CHat GPT CODE


# class Library:
#     def __init__(self):
#         self.Booklist = ["Rich dad poor dad", "Chemistry book", "C language", "Java Language"]
#         self.No_of_books = len(self.Booklist)

#     def Add_books(self):
#         new_book = input("Enter book name: ")
#         self.Booklist.append(new_book)
#         self.No_of_books += 1
#         print(f"{new_book} has been added to the library.")
#         return self.Booklist

#     def Display_available_Books(self):
#         print(f"Available books: {self.Booklist}")

#     def NoOfBooks(self):
#         print(f"No of books: {self.No_of_books}")

# Lib = Library()

# print("Initial Library State:")
# Lib.Display_available_Books()
# Lib.NoOfBooks()

# Lib.Add_books()
# print("\nUpdated Library State:")
# Lib.Display_available_Books()
# Lib.NoOfBooks()

