import random
import math

def zadanie3():
	s = input("Input line: ")
	p = s.count(' ')
	print(p)

def zadanie4():
	line = input('Enter your text: ').split()
	#for word in line:
	#	if len(word) < 4:
	#		print(word)
	words = [word for word in line if len(word) < 4]
	print(words)
	
def zadanie5():
	lista_a = [1, 2, 3, 4]
	lista_b = [2, 3, 4, 5]

	wspolne = [i for i in lista_a if i in lista_b]
	print(wspolne)

def zadanie6():
	n = int(input("Podaj liczbe: "))
	lista = [i for i in range(0, n + 1) if (i % 3 == 0 or i % 5 == 0)]
	print(lista)

def zadanie7():
	liczby = []
	n = int(input("Podaj liczbe: "))
	for i in range(n):
		i = round(random.uniform(-100, 100), 2)
		liczby.append(i)
	print(liczby)
	
	a = [i for i in liczby if i >= 0]
	print(a)
	print([int(x) for x in a])
	print([math.floor(x) for x in a])
	print([math.ceil(x) for x in a])
	print([math.log(x) for x in a])
	

def main():
	zadanie1 = [i for i in range(1000) if i % 7 == 0]
	print(f"Zadanie 1: {zadanie1}")
	zadanie2 = [i for i in range(1000) if '3' in str(i)]
	print(f"Zadanie 2: {zadanie2}")
	zadanie3()
	zadanie4()
	zadanie5()
	zadanie6()
	zadanie7()
	
main()
