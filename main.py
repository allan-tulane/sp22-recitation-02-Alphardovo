"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1
	else:
		return a*simple_work_calc(n//b,a,b)+n
	pass

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 4, 2) == 2136
	assert simple_work_calc(20, 4, 2) == 524
	assert simple_work_calc(30, 4, 4) == 74

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns
           the work done at each node

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1
	else:
		return a*work_calc(n//b,a,b,f)+f(n)
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns
           the work done at each node

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1
	else:
		return span_calc(n//2,a,b,f)+1
	pass

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(30, 2, 2,lambda n: 1) == 31
	assert work_calc(20, 1, 2, lambda n: n*n*2) == 1059 
	assert work_calc(30, 3, 2, lambda n: n**2) == 2340

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)

	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_calc(n,8,2,work_fn1),
			work_calc(n,8,2,work_fn2)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
    res = compare_work(lambda n: n**2,lambda n: n**4)
    print_results(res)

def compare_span(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	result = []
	for n in sizes:
		result.append((
			n,
			span_calc(n,8,2,work_fn1),
			span_calc(n,8,2,work_fn2)
			))
	return result

def test_compare_span():
    res = compare_span(lambda n: n**2,lambda n: n**4)
    print_results(res)
