from sys import argv

def main():
	try:
		n = int(argv[1])
	except:
		n = 10
		
	lista = [i for i in range(1, n + 1)]
	it = iter(lista)
	suma = 0
	while True:
		try:
			suma += next(it)
		except StopIteration:
			break
			
	print(suma)

if __name__== '__main__':
	main()
