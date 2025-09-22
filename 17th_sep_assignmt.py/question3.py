# problem 3:library borrow checker
# • Maintain a dictionary of available books (title → quantity).
# • Take user input for borrowing a book.
# • If the book exists and quantity > 0, issue it (reduce quantity by 1).
# • If not available, show “Out of stock” or “Not found”.
# • After all operations, write back the updated inventory to a file library.txt
library = {
    "mahabharat": 3,
    "harrypotter": 2,
    "Anne frank": 1,
    "Machine Learning": 0
}
book_title = input("Enter the title of the book you want to borrow: ")

if book_title in library:
    if library[book_title] > 0:
        library[book_title] -= 1
        print(f"Issued '{book_title}'. Please return it on time.")
    else:
        print("Out of stock.")
else:
    print("Not found.")

with open("library.txt", "w") as file:
    for title, quantity in library.items():
        file.write(f"{title}: {quantity}\n")

print("Books in 'library.txt'.")