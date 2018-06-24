class Taschenrechner:
	def addieren(self, z1, z2):
	  return z1 + z2
	def subtrahieren(self, z1, z2):
	  return z1 - z2
	def dividieren(self, z1,z2):
	  return z1 / z2
	def multiplizieren(self, z1, z2):
	  return z1 * z2



def main():
	t = Taschenrechner()
	result = 0
		
	z1 = float(raw_input("Zahl eingeben:"))
	op1 = raw_input("Operation:")
	z2 = float(raw_input("Zahl eingeben: "))

	if op1 == "+":
		result = t.addieren(z1, z2)
	elif op1 == "-":
		result = t.subtrahieren(z1, z2)
	elif op1 == "/":
		result = t.dividieren(z1, z2)
	elif op1 == "*":
		result = t.multiplizieren(z1, z2)
		
	op2 = ""
	while op2.lower() != "ende":
		op2 = raw_input("2. Operation oder 'ende' eingeben: ")
		
		if op2 == "ende":
			break
		
		z3 = float(raw_input("Zahl eingeben:"))
		
		if op2 == "+":
			result = t.addieren(result, z3)
		elif op2 == "-":
			result = t.subtrahieren(result, z3)
		elif op2 == "/":
			result = t.dividieren(result, z3)
		elif op2 == "*":
			result = t.multiplizieren(result, z3)
		
	print result
			
			
if __name__ == "__main__":
	main()
	

	