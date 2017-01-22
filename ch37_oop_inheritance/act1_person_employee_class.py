class Person():
	"""docstring for Person"""
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last

	def Name(self):
		return self.firstname + " " + self.lastname

class Employee(Person):
	"""docstring for Employee"""
	def __init__(self, first, last, staffnum):
		super().__init__(first, last)
		self.staffnumber = staffnum
	
	def GetEmployee(self):
		return self.Name() + ", " + self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())
