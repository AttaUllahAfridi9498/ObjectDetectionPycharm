
book_inventory = []

#Adding a new book
def add_book():
	title = input("Enter book title: ")
	author = input("Enter book author: ")
	price = float(input("Enter book price: "))
	book = {"title": title, "author": author, "price": price}
	book_inventory.append(book)
	print("Book added successfully!")

# Function to display all books
def display_books():
	print("Books in inventory:")
	for book in book_inventory:
		print(book)

# Function to search for a book
def search_book():
	title = input("Enter book title to search: ")
	for book in book_inventory:
		if book["title"] == title:
			print(book)
			return
	print("Book not found!")


def update_book():
    title = input("Enter book title to update: ")
    for book in book_inventory:
        if book["title"] == title:
            print("Book found. Enter new details:")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_price = float(input("Enter new price: "))

            book["title"] = new_title
            book["author"] = new_author
            book["price"] = new_price

            print("Book details updated successfully!")
            return
    print("Book not found!")
# Function to remove a book
def remove_book():
	title = input("Enter book title to remove: ")
	for book in book_inventory:
		if book["title"] == title:
			book_inventory.remove(book)
			print("Book removed successfully!")
			return
	print("Book not found!")

# Main menu
while True:
	print("\nBook Inventory System")
	print("1. Add a new book")
	print("2. Display all books")
	print("3. Search for a book")
	print("4. Update a book price")
	print("5. Remove a book")
	choice = input("Choose an option: ")
	if choice == "1":
		add_book()
	elif choice == "2":
		display_books()
	elif choice == "3":
		search_book()
	elif choice == "4":
		update_book()
	elif choice == "5":
		remove_book()
	else:
		print("Invalid choice. Please try again.")

