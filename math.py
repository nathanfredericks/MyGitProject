def recursiveFibonacci(int num):
	#if you are asking for the 0th Fibonacci number, return 1
	if(num == 0):
		return 1
	#if you are asking for the first Fibonacci number, return 1
	if(num == 1):
		return 1
	#recursively calls itself until it gets to num == 1 and num == 0
	return (recursiveFibonacci(num - 1) + recursiveFibonacci(num - 2))
