# performance-test

try to compare speed of multiplying two matrixes, with simple method using for loops and with numpy 

time measured with timeit module

results:

-matrixes 10x10:
	-Multiply with multiply_my_way:  0.001s
	-Multiply with multiply_with_numpy:  0.0007s

-matrixes 100x100:
	Multiply with multiply_my_way:  0.3295s
	Multiply with multiply_with_numpy:  0.0412s

-matrixes 1000x1000:	
	Multiply with multiply_my_way:  343.634s
	Multiply with multiply_with_numpy:  5.5368s


