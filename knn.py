#import get_feature
from sklearn.svm import SVC
from random import shuffle
import numpy as np
import random
from operator import itemgetter
data = []

def get_data():
	fo = open('quotes.txt','r+')
	a = fo.readlines()
	a = [x for x in a if x!='\n']
	for line in a:
		data.append(line[:-1] + '\t' +'0')
	fo.close()

	fo = open('jokes.txt','r+')
	a = fo.readlines()
	a = [x for x in a if x!='\n']
	for line in a:
		data.append(line[:-1] + '\t' + '1')
	fo.close()
	shuffle(data)
	print len(data)

def separate_data(test_start,test_end):
	train_feature_matrix = []
	test_feature_matrix = []
	train_data_matrix = []
	test_data_matrix = []
	for j in xrange(len(data)):
		basic_matrix = [get_feature.check_alliteration(data[j][:-1]), get_feature.check_antonyms(data[j][:-1]), get_feature.check_slang(data[j][:-1])]
		if j>= test_start and j<= test_end:
			test_data_matrix.append(data[j])
			test_feature_matrix.append(basic_matrix)
		else:
			train_data_matrix.append(int(data[j][-1]))
			train_feature_matrix.append(basic_matrix)
	return [train_data_matrix,train_feature_matrix,test_data_matrix,test_feature_matrix]
def closest_diff(sentence,train_set):
	total_words=1000.0	
	l=[]
	for s in train_set:
		q=sentence.split()
		q.pop()
		w=s.split()
		flag=w[-1]
		w.pop()
		t = list(set(q[:]) & set(w))
		count1,count2=0.0,0.0
		
		if flag=="1":
			count1=len(t)/total_words
		else:
			count2=len(t)/total_words
		diff=count1-count2
		if diff<0:
			diff=-diff
		#print count1-count2,flag
		l.append((diff,q,flag))
	l.sort(key=itemgetter(0))
	#print "sorted"
	l2=l[:5]
	joke,not_joke=0,0
	for i in l2:
		if i[-1]=="1":
			joke=joke+1
		else:
			not_joke=not_joke+1
	if joke>not_joke:
		return "1"
	else:
		return "0"
def main():
	get_data()
	for i in xrange(10):
		print "Fold:",i+1
		accuracy = 0
		test_count = 0
		test_start = (9-i)*(52165/10) 
		test_end =  (10-i)*(52165/10) - 1
		test_data,train_data=[],[]
		for j in range(len(data)):
			#print data[j]
			x=random.random()
			#print x
			if x<0.2:
				test_data.append(data[j])
			else:
				train_data.append(data[j])
		test_count=len(test_data)	
		accuracy=0.0
		count=0
		for sentence in test_data:
			flag=closest_diff(sentence,train_data)
			if flag==sentence.split()[-1]:
				accuracy+=1.0
		print len(test_data),len(train_data)
		print "Accuracy: + " + str(accuracy) + " Total: " + str(test_count)
		print "Percent:",(accuracy/test_count)*100
		
		

main()
