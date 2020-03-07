import threading

x=0

def increment():
	global x
	x+=1

def thread_task(lock):
	for i in range(1000):
		lock.acquire() 	# get access to critical section
		increment() # uses a global variable
		lock.release() # release access from critical section

def main_task():
	global x
	x=0
	#creating a lock
	lock=threading.Lock()
	#creating threads
	thread_1=threading.Thread(target=thread_task,args=(lock,))
	thread_2=threading.Thread(target=thread_task,args=(lock,))
	thread_1.start()
	thread_2.start()
	thread_1.join()
	thread_2.join()

if __name__=='__main__':
	for i in range(10):
		main_task()
		print(i,x)
