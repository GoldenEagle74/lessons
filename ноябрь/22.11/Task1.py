"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""
class BankAccount:
	def __init__(self,name,balance,pasport):
		self._name = name
		self.__balance = balance
		self.__pasport = pasport
		self.password = None
	def getpasport(self): return self.__pasport
	def getbalance(self): return self.__balance
	def setpasport(self,newpasport):
		if self.password == None: self.password = input('Введите новый пароль: ')
		if input('Введите текущий пароль: ') == self.password: self.__pasport = newpasport
	def setbalance(self,newbalance):
		if newbalance>0: self.__balance = newbalance
	def delpasport(self):
		if self.password == None: self.password = input('Введите новый пароль: ')
		if input('Введите текущий пароль: ') == self.password: del self.__pasport		
