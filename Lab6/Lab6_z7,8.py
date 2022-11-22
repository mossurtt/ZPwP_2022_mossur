def fib(n):
	result = [1, 1]
	for i in range(n - 2):
		result.append(result[i] + result[(i + 1)])
		
	return result

L = fib(10)
parzyste = filter(lambda x: x % 2 == 0, L)
print(list(parzyste))

nieparzyste = filter(lambda x: x % 2 == 1, L)
print(list(nieparzyste))
	

	
