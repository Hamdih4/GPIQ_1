#!/usr/bin/python

import json

def get_state():
	book_id = raw_input("Enter the book id to search for: ")
	try:
		with open('book_details.json', 'r') as books_file:
			book_details = json.load(books_file)
		state = book_details[book_id]
		return book_id, state
	
	except KeyError:
	 	print("Invalid Book ID.")
	 	return 0, 0
	
def update_state(book_id, state):
	with open('book_details.json', 'r+') as books_file:
		book_details = json.load(books_file)	
		book_details[book_id] = state
		books_file.seek(0)
		books_file.write(json.dumps(book_details))

def search_book():
	book_id, state = get_state()
	if book_id != 0:
		if(state == "B"):
			print(book_id, " Borrowed")
		elif (state == "A"):
			print(book_id, " Available")
		elif (state == "R"):
			print(book_id, " Returned")

def borrow_book():
	book_id, state = get_state()
	if book_id != 0:
		if(state == "B"):
			print("Sorry, you cannot borrow this time, the book is not available.")
		elif (state == "A"):
			update_state(book_id, "B")
			print(book_id, " Available, successfully borrowed by you.")
		elif (state == "R"):
			print(book_id, "Returned. Wait for the book to be Available again.")

def return_book():
	book_id, state = get_state()
	if book_id != 0:
		if(state == "A"):
			print(book_id, "Available, you cannot return a book that is already available.")
		elif (state == "B"):
			update_state(book_id, "R")
			print(book_id, " Borrowed, successfully returned by you.")
		elif (state == "R"):
			print(book_id, "Returned, you cannot return a book that was already returned.")

while 1:
	print("\n\nWhat do you want to do today? \n(S)earch for a book? \n(B)orrow a book? \n(R)eturn a book? \n(E)xit")
	choice = raw_input()
	if(choice == "S"):
		search_book()
	elif(choice == "B"):
		borrow_book()
	elif(choice == "R"):
		return_book()
	elif(choice == "E"):
		break
	else:
		print("Invalid Input")
