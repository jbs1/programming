"""Jeremy Schulz"""
import dllist as dl
import insertion as ins
import random as rn
import time

def test(sort,r=250):
	"""function to test various sorts"""
	test=dl.dllist();
	test1=dl.dllist();
	test2=dl.dllist();


	# sorted
	for i in range(r):
		test.ins_tl(i)
	print("Testing sorted({0}):".format(r))
	t1=time.perf_counter()
	sort(test)
	t2=time.perf_counter()
	print("Result: {0} sec".format(t2-t1))

	# # rev. sorted
	for i in range(r):
		test1.ins_hd(i)
	print("Testing reverse-sorted({0}):".format(r))
	t1=time.perf_counter()
	sort(test1)
	t2=time.perf_counter()
	print("Result: {0} sec".format(t2-t1))

	# # random
	for i in range(r):
		test2.ins_tl(rn.randrange(r*30))
	print("Testing random({0}):".format(r))
	t1=time.perf_counter()
	sort(test2)
	t2=time.perf_counter()
	print("Result: {0} sec".format(t2-t1))


test(ins.insertionsort)