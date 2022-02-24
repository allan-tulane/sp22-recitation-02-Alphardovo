from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 4, 2) == 2136
	assert simple_work_calc(20, 4, 2) == 524
	assert simple_work_calc(30, 4, 4) == 74

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(30, 2, 2,lambda n: 1) == 31
	assert work_calc(20, 1, 2, lambda n: n*n*2) == 1059 
	assert work_calc(30, 3, 2, lambda n: n**2) == 2340

test_compare_span()
test_compare_work()
test_simple_work()
test_work()
