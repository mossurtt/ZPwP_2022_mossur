miasta = ['Lutsk', 'Czestochowa', 'Kyiv', 'Warszawa', 'Lviv', 'Krakow']
it = iter(miasta)

while True:
	try:
		miasto = next(it)
		print(miasto)
	except StopIteration:
		break
		

