"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""

class Profile:
	def __init__(self,name,last_name,age,passport):
		self.name = name
		self.last_name = last_name
		self.age = age
		self.passport = passport
		
class Address:
	def __init__(self, city, street, zipcode):
		self.city = city
		self.street = street
		self.zipcode = zipcode
		
class Role:
	def __init__(self,role,hours_worked):
		self.role = role
		self.hours_worked = hours_worked
		
class BankAccount:
	def __init__(self,card_number, balance):
		self.card_number = card_number
		self.balance = balance
		
class Order:
	def __init__(self,item,date,delivery,price):
		self.item = item
		self.date = date
		self.delivery = delivery
		self.price = price
		
class User:
	def __init__(self):
		self.order = []
	def create_profile(self,name,last_name,age,passport):
		self.profile = Profile(name, last_name, age, passport)

	def add_address(self, city, street, zipcode):
		self.address = Address(city, street, zipcode)
		
	def set_role(self, role, hours_worked):
		self.role = Role(role, hours_worked)
	
	def add_bankaccount(self, card_number, balance):
		self.bankaccount= BankAccount(card_number, balance)
		
	def create_order(self, item, date, delivery, price):
		self.order.append(Order(item, date, delivery, price))
