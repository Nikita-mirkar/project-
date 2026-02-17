from library import Library

class LibrarySystem:
    def __init__(self):
        self.lib = Library()

    def admin_menu(self):
        uid = input("Enter user name: ")
        pass1 = input("Enter password: ")

        if uid == "Nikita" and pass1 == "Nikita123":
            while True:
                print("\n ADMIN MENU")
                print("1. Add Book")
                print("2. Display Books")
                print("3. Search Book")
                print("4. Delete Book")
                print("5. Update Book")
                print("6. Borrow Book")
                print("7. Return Book")
                print("8. Exit Admin")

                try:
                    choice = int(input("Enter choice: "))
                except ValueError:
                    print("Please enter a valid number")
                    continue

                if choice == 1:
                    self.lib.addbook()
                elif choice == 2:
                    self.lib.display()
                elif choice == 3:
                    self.lib.searchbook()
                elif choice == 4:
                    self.lib.deletebook()
                elif choice == 5:
                    self.lib.updatebook()
                elif choice == 6:
                    self.lib.borrowbook()
                elif choice == 7:
                    self.lib.returnbook()
                elif choice == 8:
                    print("Exiting Admin Menu...")
                    break
                else:
                    print("Invalid choice")
        else:
            print("Invalid Username or Password")

        uid = input("Enter user name: ")
        pass1 = input("Enter password: ")

        if uid == "Nikita" and pass1 == "Nikita123":
            while True:
                print("\n USER MENU")
                print("1. Display Books")
                print("2. Search Book")
                print("3. Exit User")

                try:
                    choice = int(input("Enter choice: "))
                except ValueError:
                    print("Please enter a valid number")
                    continue

                if choice == 1:
                    self.lib.display()
                elif choice == 2:
                    self.lib.searchbook()
                elif choice == 3:
                    print("Exiting User Menu...")
                    break
                else:
                    print("Invalid choice")
        else:
            print("Invalid Username or Password")

    def main_menu(self):
        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Admin Login")
            print("2. User Login")
            print("3. Exit")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Invalid input")
                continue

            if choice == 1:
                self.admin_menu()
            elif choice == 2:
                self.user_menu()
            elif choice == 3:
                print("Thank you 🙏")
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    system = LibrarySystem()
    system.main_menu()




