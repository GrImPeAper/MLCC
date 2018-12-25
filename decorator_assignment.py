
def logged(func):
	def inner(*args,**kwargs):
		print('You called ',func.__name__,*kwargs,args)
		print ('It returned ',func(*args))
	return inner

@logged
def func(*args):
	return 3 + len(args)

@logged
def prod(*args):
	return args[0]*args[1]
func(4,4,4)
prod(4,5)

