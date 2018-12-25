import multiprocessing
lock = multiprocessing.Lock()
def squ(x):
	lock.acquire()
	try:
		no = x**2
		print('{0} is squared to {1} by: {2}'.format(x,no,multiprocessing.current_process().name))
		return no
	finally:
		lock.release()
	
if __name__=='__main__':
	#q = multiprocessing.Array(0,range(1,11))
	pool = multiprocessing.Pool(processes = len(range(1,11)))
	res = [pool.apply_async(squ,(x,)) for x in range(10)]
	print ([results.get(timeout=1) for results in res])
	#for i in range(1,11):
		
