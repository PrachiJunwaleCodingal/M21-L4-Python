#ACP-Class string reverse

class ClsRev:

	def __init__(self, w):
		self.s = w
		
	def revWrd(self):
		return self.s[::-1]

word = input("Enter word to be reversed : ")
rev_ob = ClsRev(word)
result = rev_ob.revWrd()
print("Reversed String :", result)
