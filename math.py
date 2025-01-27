def recursiveFibonacci(int num):
	if(num == 0):
		return 1
	if(num == 1):
		return 1
	return (recursiveFibonacci(num - 1) + recursiveFibonacci(num - 2))
