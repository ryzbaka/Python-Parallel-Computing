import threading

def print_cube(x):
	print(x**3)

def print_square(x):
	print(x**2)

if __name__=='__main__':
	thread_1=threading.Thread(target=print_square,args=(10,))
	thread_2=threading.Thread(target=print_cube,args=(10,))
	thread_1.start()
	thread_2.start()
	thread_1.join() # wait for thread 1 to end
	thread_2.join() # wait for thread 2 to end
	print('done!')
