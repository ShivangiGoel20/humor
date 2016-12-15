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
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer.strip()

def compareTwoStrings(string1, string2):
    list1 = list(string1)
    list2 = list(string2)

    match = []
    output = ""
    length = 0

    for i in range(0, len(list1)):

        if list1[i] in list2:
            match.append(list1[i])

            for j in range(i + 1, len(list1)):

                if ''.join(list1[i:j]) in string2:
                    match.append(''.join(list1[i:j]))

                else:
                    continue
        else:
            continue

    for string in match:

        if length < len(list(string)):
            length = len(list(string))
            output = string

        else:
            continue

    return output.strip()
def main():
	get_data()
	idioms=[]
	f = open('idioms.txt','r+')
	a = f.readlines()
	a = [x for x in a if x!='\n']
	for line in a:
		idioms.append(line.strip())
	f.close()
	print len(idioms)
	#print idioms
	for i in xrange(10):
		print "Fold:",i+1
		accuracy = 0
		test_count = 0
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
		for sentence in test_data[:10]:
			for i in idioms:
				s=compareTwoStrings(sentence,i)
				s2=longestSubstringFinder(sentence,i)
				print s,"***",s2
		print len(test_data),len(train_data)
		
		print "Accuracy: + " + str(accuracy) + " Total: " + str(test_count)
		print "Percent:",(accuracy/test_count)*100
		
		
		
		

main()
