import numpy as np
import math

#Rastrigin's Function
def rastrigins(x,y,z):
	for i in range(len(x)):
		for j in range(len(y)):
			z[i][j] = 20 + (x[i] * x[i]) +  (y[j] * y[j]) - 10  * (math.cos(2 * math.pi * x[i]) + math.cos(2 * math.pi *y[j])) 		

def sphere(x,y):
	for i in range(len(x)):
		y[i] = x[i] * x[i]
		
def rosenbrock(x,y):	
	for i in range(len(x) - 1):
		y[i] = 100 * ( math.pow(math.pow(x[i],2) - x[i+1],2)) + math.pow(1 - x[i],2) 
