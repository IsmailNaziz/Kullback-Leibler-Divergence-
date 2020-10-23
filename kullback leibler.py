# -*- coding: utf-8 -*-
"""
@author: Naziz Ismail 
"""


import pandas as pd
import numpy as np 

def p(x):
	return

def q(x):
	return 

def div_kullback_leibler(p,q,nb_step,bounds):
	sum = 0
	# interval [a,b] is the sum from - infinite to infinite 
	a = max(bounds)
	b = min(bounds)
	interval = int((a-b)/nb_step)
	# right rectangles
	for i in range(nb_step):
		x = a + i*interval
		sum = interval* p(x)*np.log(p(x)/q(x))

	return sum

def symetric_div_kullback_leibler(p,q,nb_step,bounds):
	return div_kullback_leibler(p,q,nb_step,bounds) + div_kullback_leibler(q,p,nb_step,bounds)

def multi_dim_div_kullback_leibler(p,q,nb_step,bounds):
	sum = 0
	# interval [a,b] is the sum from - infinite to infinite 
	for j in range(len(bounds)):
		a = max(bounds[j])
		b = min(bound[j])
		interval = int((a-b)/nb_step[j])
		# right rectangles
		for i in range(nb_step):
			x = a + i*interval
			sum = interval* p(x)*np.log(p(x)/q(x))

	return sum