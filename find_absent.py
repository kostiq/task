def find_absent(array):
	for i, number in enumerate(array, start=1):
		if number - array[i-2] == 2:
			yield number - 1

if __name__ == '__main__':
	for number in find_absent([1,2,4,5,6,8,10]):
		print(number)
