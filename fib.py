def recursiveFibonacci(num):
	#if you are asking for the 0th Fibonacci number, return 1
	if(num == 0):
		return 1
	#if you are asking for the first Fibonacci number, return 1
	if(num == 1):
		return 1
	#recursively calls itself until it gets to num == 1 and num == 0
	return (recursiveFibonacci(num - 1) + recursiveFibonacci(num - 2))

def iterativeFibonacci(num):
    # If the requested number is 0 or 1, return 1
    if num == 0 or num == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    fib_0 = 1
    fib_1 = 1

    # Calculate Fibonacci iteratively up to the desired number
    for _ in range(2, num + 1):
        fib_next = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib_next

    return fib_1
