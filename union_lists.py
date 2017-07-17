def union_lists(list1, list2):
	list1 = set(list1)
	list2 = set(list2)

	return list(list1 | list2)

if __name__ == '__main__':
	print(union_lists([1,2,3], [1, 3]))