library = {}
while True:
    print("1. Add Book\n2. Remove Book\n3. View Books\n4. Borrow Book\n5. Return Book\n6. Exit")
    choice = input(" Select One : ")
    if (choice == "1"):
        title = input("Write your book title : ").lower()
        library[title] = "Avalaible"
        print(f"Successfull! {title} has been added")
    elif (choice == "2"):
        remove_books = input("Write book title you want to remove : ").lower()
        if remove_books in library:
            del library[remove_books]
            print(f"{remove_books} has been removed successfully")
        else:
            print(f"Error {remove_books} did't found in the library")
    elif (choice == "3"):
        print("----Avalaible Books----")
        for books, status in library.items():
            print(f"{books} - {status}")
    elif (choice == "4"):
        borrow_books = input(" Write book title : ").lower()
        if borrow_books in library:
            library[borrow_books] = "Borrowed"
            print(f"Book {borrow_books} has borrowed successfully")
    elif (choice == "5"):
        return_books = input("Put books title here : ").lower()
        if return_books in library:
            library[return_books] = "Avalaible"
            print(f"Book {return_books} has returned successfully")
    elif (choice == "6"):
        print("----Exit Successfully----")
        break
    else:
        print("----Invalid Choice----")

print("----Thank You For Using----")
    
        
    