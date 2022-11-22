from Temperature import temperature

def main():

	t = temperature(9)
	print(t._temperature__temp)
	t = t + 12
	print(t)
	t = 6 + t
	print(t)
	t += 3
	print(t)

main()
