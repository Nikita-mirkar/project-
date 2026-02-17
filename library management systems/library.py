from book import Book
from datetime import date
from prettytable import PrettyTable

class Library:
    def __init__(self):
        self.name = "FBS Library"
        self.books_file = "data.txt"

    def addbook(self):
        bid = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        price = float(input("Enter Book Price: "))
        added_date = date.today()
        status = "Available"
        b = Book(bid, title, author, price, added_date)

        with open(self.books_file, "a") as f:
            f.write(f"{b.bid},{b.title},{b.author},{b.price},{b.added_date},{status}\n")
        print("Book added successfully!")

    def display(self):
        table = PrettyTable()
        table.field_names = ["ID", "Title", "Author", "Price", "Added Date", "Status"]
        rows_added = 0  

        try:
            with open(self.books_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue 


                    data = [item.strip() for item in line.split(",")]

                
                    while data and data[-1] == "":
                        data.pop()

                    if len(data) != 6:
                        continue  

                    table.add_row(data)
                    rows_added += 1

            if rows_added == 0:
                print("No books found!")
            else:
                print(table)

        except FileNotFoundError:
            print("Books file not found!")

    def searchbook(self):
        try:
            book_id = input("Enter book ID to search: ").strip()
            found = False
            table = PrettyTable()
            table.field_names = ["ID", "Title", "Author", "Price", "Added Date", "Status"]

            with open(self.books_file, "r") as f:
                for line in f:
                    data = [item.strip() for item in line.split(",")]

                    while data and data[-1] == "":
                        data.pop()

                    if len(data) != 6:
                        continue

                    if data[0] == book_id:
                        table.add_row(data)
                        found = True
                        break

            if found:
                print("\nBook found:")
                print(table)
            else:
                print("\nBook not found!")
                print("1. Search again")
                print("2. Go back to Admin Menu")
                choice = input("Enter choice: ")

                if choice == "1":
                    self.searchbook()
                else:
                    return  

        except FileNotFoundError:
            print("No books found!")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    def updatebook(self):
        bid = input("ENTER BOOK ID TO UPDATE: ")
        found = False
        store = []
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(",")
                    if data[0] == str(bid):
                        found = True
                        print("1. Update Title\n2. Update Author\n3. Update Price")
                        ch = int(input("Enter choice: "))
                        if ch == 1:
                            data[1] = input("ENTER NEW TITLE: ")
                        elif ch == 2:
                            data[2] = input("ENTER NEW AUTHOR: ")
                        elif ch == 3:
                            data[3] = input("ENTER NEW PRICE: ")
                        else:
                            print("Invalid option")
                    store.append(",".join(data) + "\n")
            if found:
                with open("data.txt", "w") as f:
                    f.writelines(store)
                print("BOOK UPDATED SUCCESSFULLY")
            else:
                print("BOOK NOT FOUND")
        except FileNotFoundError:
            print("No books found!")

    def deletebook(self):
        bid = input("ENTER BOOK ID TO DELETE: ")
        found = False
        store = []
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(",")
                    if data[0] != str(bid):
                        store.append(",".join(data) + "\n")
                    else:
                        found = True
            if found:
                with open("data.txt", "w") as f:
                    f.writelines(store)
                print("BOOK DELETED SUCCESSFULLY")
            else:
                print("BOOK NOT FOUND")
        except FileNotFoundError:
            print("No books found!")

    def borrowbook(self):
        bid = input("ENTER BOOK ID TO BORROW: ")
        user = input("ENTER YOUR NAME: ")
        found = False
        store = []

        try:
            with open("data.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(",")

                    while len(data) < 7:
                        data.append("")

                    if data[0] == str(bid):
                        if data[5] == "Available":
                            data[5] = "Borrowed"
                            data[6] = user
                            found = True
                            print(f"BOOK BORROWED SUCCESSFULLY BY {user}")
                        else:
                            print(f"BOOK IS ALREADY BORROWED BY {data[6]}")
                            found = True

                    store.append(",".join(data) + "\n")

            if found:
                with open("data.txt", "w") as f:
                    f.writelines(store)
            else:
                print("\nBOOK NOT FOUND!")
                print("1. Try again")
                print("2. Go to Admin Menu")
                choice = input("Enter choice: ")

                if choice == "1":
                    self.borrowbook()
                else:
                    return

        except FileNotFoundError:
            print("No books found!")
            return


    def returnbook(self):
        bid = input("ENTER BOOK ID TO RETURN: ")
        user = input("ENTER YOUR NAME: ")
        found = False
        store = []

        try:
            with open("data.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(",")

                    while len(data) < 7:
                        data.append("")

                    if data[0] == str(bid):
                        if data[5] == "Borrowed":
                            if data[6] == user:
                                data[5] = "Available"
                                data[6] = ""
                                found = True
                                print(f"BOOK RETURNED SUCCESSFULLY BY {user}")
                            else:
                                print(f"BOOK WAS BORROWED BY {data[6]}, NOT {user}")
                                found = True
                        else:
                            print("BOOK WAS NOT BORROWED")
                            found = True

                    store.append(",".join(data) + "\n")

            if found:
                with open("data.txt", "w") as f:
                    f.writelines(store)
            else:
                print("\nBOOK NOT FOUND!")
                print("1. Try again")
                print("2. Go to Admin Menu")
                choice = input("Enter choice: ")

                if choice == "1":
                    self.returnbook()
                else:
                    return

        except FileNotFoundError:
            print("No books found!")
            return
