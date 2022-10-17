def mult(L):
	il = 1
	for i in L:
		il *= i
	return il
	
def mult_ints(L):
	il = 1
	for i in L:
		if isinstance(i, int):
			il *= i
	return il
	
def multiply(*args):
	mult = 1
	for i in args:
		mult *= i
	return mult
	
def multiply_ints(*args):
	mult = 1
	for i in args:
		if isinstance(i, int):
			mult *= i
	return mult
	

def make_car(firma, model, **kwargs):
	return dict(firma = firma, model = model, **kwargs)
	

def main():
	print(mult([3, 5, 7]))
	print(mult(range(2, 8, 2)))
	print(mult_ints([3, 3.14, 5, "abc", 7]))
	print(multiply(3, 5, 7))
	print(multiply_ints(3, 3.14, 5, "abc", 7))
	print(make_car("Kia", "Picanto", kolor = "cafe mocca", poj_silnika = 900))

main()

