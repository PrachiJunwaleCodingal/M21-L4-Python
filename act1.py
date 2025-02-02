#keep it private

class cls1:
	__pVar = 50
	def __method(self):
		print("Inside class")

	def fun1(self):
		print("Private Var: ",cls1.__pVar)

obj = cls1()
obj.fun1()
obj.__method    #gives error as private