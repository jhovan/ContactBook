#Gallardo Valdez Jose Jhovan
#06/09/2016
#Contact book

import re

class invalidEmail(Exception):
	pass

class invalidNumber(Exception):
	pass

#asks for a telephone number
def askNumber(message):
	while True:
			try:
				number=raw_input(message)
				if len(number)!= 10:
					raise invalidNumber
				number=int(number) 
				return number
			except ValueError:
				print "Invalid number, it's not an integer, try again"
			except invalidNumber:
				print "The number should have ten digits, try again"

#asks for an email
def askEmail():
	while True:
		try:
			email=raw_input("Write an email:")
			if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()):
				return email
			else:
				raise invalidEmail
		except invalidEmail:
			print "Invalid email, try again"


#Class person that represents a person and his data
class Person:

#constructor of the class
	def __init__(self, data):
		self.name=data[0]
		self.surname=data[1]
		self.home=data[2]
		self.mobile=data[3]
		self.email=data[4]

#to string method
	def __str__(self):
		return "\n" + self.name + " " + self.surname + "\n" + str(self.home) + "\n" + str(self.mobile) + "\n" + self.email + "\n"

#returns a string with the data to save in a file
	def data(self):
		return self.name + "-" +self.surname + "-" + str(self.home) + "-" + str(self.mobile) + "-" + self.email + "-"

#class book that represents a contact book
class Book:

#constructor of the class
	def __init__(self,name):
		self.list=[]
		self.name=name

#reads the file and takes the data from the file
	def read(self):
		self.list=[]
		f=open(self.name + ".txt","r")
		for line in f.readlines():
			if len(line) > 1:
				self.list.append(Person(line.split("-")))
		f.close()

#writes the data to the file
	def write(self):
		f=open(self.name + ".txt","w")
		for person in self.list:
			f.write(person.data() + "\n")
		f.close()

#show all the contacts in the book
	def show(self):
		self.read()
		for person in self.list:
			print str(person) 
		if len(self.list)==0:
			print "The book is empty"

#add a new contact to the book (and ask for the data)
	def add(self):
		self.read()
		data=[]
		data.append(raw_input("Write the name(s):"))
		data.append(raw_input("Write the surname(s):"))
		data.append(askNumber("Write the home telephone number:"))
		data.append(askNumber("Write the mobile number:"))
		data.append(askEmail())
		self.list.append(Person(data))
		self.write()

#looks for coincidences in the contacts
	def searchCoincidences(self):
		name=raw_input("Write what you want to search:")
		self.read()
		c=0
		for person in self.list:
			if (name in person.name) or (name in person.surname):
				c+=1
				print str(person) 

		if c==0:
			print "No coincidences"

#return a person after asking for his name
	def buscarNameSurname(self):
		name=raw_input("Write the name(s):")
		surname=raw_input("Write the surname(s):")
		self.read()
		for person in self.list:
			if person.name==name and person.surname==surname:
				return person
		print "Contact not found"
		return None

#deletes a person from the book
	def delete(self):
		person=self.buscarNameSurname()
		if person != None:
			self.list.remove(person)
			print "Contact deleted"
		self.write()

#deletes all the persons in the book
	def deleteAll(self):
		self.list=[]
		self.write()

#allows the user to edit a contact
	def edit(self):
		person=self.buscarNameSurname()
		if person != None:
			op=input("Choose a number:\n1.Name(s)\n2.Surname(s)\n3.Home number\n4.Mobile number\n5.Email\n")
			if op==1:
				name=raw_input("Write the name(s):")
				person.name=name
				print "name updated"
			elif op==2:
				surname=raw_input("Write the surname(s):")
				person.surname=surname
				print "surname updated"
			elif op==3:
				person.home=askNumber("Write the home number:")
				print "home number updated"
			elif op==4:
				person.mobile=askNumber("Write the mobile number:")
				print "mobile number updated"
			elif op==5:
				person.email=askEmail()
				print "email updated"
			else:
				print "invalid choice"
			self.write()


#Opens a book (the file it's in the same directory that the code)
while True:
	try:
		name=raw_input("Write the name of the book:")
		book=Book(name)
		book.read()
		print "Book opened"
		break
	except:
		dec=input("The book doesn't exist, do you want to create it?\n1.Yes\n2.No\n")
		if dec==1:
			book.write()
			break

#Main menu
op=1

while(op!=7):
	op=input("Choose a number:\n1.Add contact\n2.Search contact\n3.Delete contact\n4.Edit contact\n5.Show all contacts\n6.Delete all contacts\n7.Exit\n")
	if(op==1):
		book.add()
		print "Contact added"
	elif(op==2):
		book.searchCoincidences()
	elif(op==3):
		book.delete()
	elif(op==4):
		book.edit()
	elif(op==5):
		book.show()
	elif(op==6):
		dec=input("Are you sure?\n1.Yes\n2.No\n")
		if dec==1:
			book.deleteAll()
			print "The book is empty"
	elif(op!=7):
		print "Invalid choice"