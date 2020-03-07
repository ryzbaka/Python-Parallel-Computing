from multiprocessing import Process,Value,Lock

def withdraw(balance,lock):
	lock.acquire()
	for _ in range(1000):
		balance.value-=1
	lock.release()

def deposit(balance,lock):
	lock.acquire()
	for _ in range(1000):
		balance.value+=1
	lock.release()

def perform_transactions():
	lock=Lock()
	balance=Value('i',100) #initial balance which is a shared resource

	p1=Process(target=withdraw,args=(balance,lock))
	p2=Process(target=deposit,args=(balance,lock))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	print(balance.value)

if __name__=='__main__':
	for i in range(10):
		perform_transactions()

