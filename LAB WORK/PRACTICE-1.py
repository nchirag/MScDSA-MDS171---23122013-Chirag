class book :
    def __init__(self,author,title,quantity):
        self.author = author
        self.title = title
        self.quantity = quantity

    def __str__(self):
        return f"Title : {title},Author: {author},Quantity : {quantity}"
    
    class LMS:
        def __init__(self):
            self.books = []

        def add_book(self):
            title = eval(input("enter the name "))
            author = input()
            quantity = int(input())
            book = books(title,author,quantity)
            self.books.append(book)
        def borrow_book(self,title):
            for book in self.books :
                if self.title == title :
                    self.books -= 1
                    print("Book borrowed successfully")
                return
            
        def return_book(self,title):
            for book in self.books:
                if self.books == title :
                    self.book += 1
                    print("Book returned successfully")
                return
        def list_book(self):
            if self.books:
                print("List of books")
            else :
                print("The lib is empty")
        def display(self):
            while True :
            
                print("\nLibrary Management Menu:")
                print("1. Add Book")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. Display Inventory")
                print("5. Exit")

                choice = input("Enter your choice (1/2/3/4/5): ")

                if choice == "1":
                    title = input("Enter the title of the book: ")
                    author = input("Enter the author of the book: ")
                    quantity = int(input("Enter the quantity of the book: "))
                    self.add_book(title, author, quantity)
                elif choice == "2":
                    title = input("Enter the title of the book to borrow: ")
                    self.borrow_book(title)
                elif choice == "3":
                    title = input("Enter the title of the book to return: ")
                    self.return_book(title)
                elif choice == "4":
                    self.display_inventory()
                elif choice == "5":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library = LMS()
    library.display()



            

