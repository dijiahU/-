a = int(input('输入第几号元素：'))
def fibonacci(x):
	list =[]
	for i in range(x):
		if i ==0 or i==1:
			list.append(1)
		else:
			list.append(list[i-2]+list[i-1])
	return list[x-1]
print(fibonacci(a))