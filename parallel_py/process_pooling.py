import multiprocessing
import os

def f(x):
	something=x*x
	return something
if __name__=='__main__':
	input_list=[1,2,3,4,5,5,3,22,2,34,3,2,2]

	process_pool=multiprocessing.Pool()

	result=process_pool.map(f,input_list)

	print(result)
