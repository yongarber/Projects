# process-
# 1. extract the columns (text, title, and type) using pandas and numpy
# 2. while (type != null) make directory with function that make CSV files of title and text.
# 3. make function that convert the title and text into a csv file.
# 4. make a list of all the kinds
# need tp think what to do with the list of type
import pandas as pd
import numpy as np
import os


Data = pd.read_csv("fake-Kaggle.csv", usecols = ['title','text','type']) 
data=Data.sort_values(by=['type'])
data.to_csv('AfterSort.csv')
title = data['title']
text = data['text']
Type = data['type']

ListArray=data['type'].value_counts()
# this variable contains an array with type and count. I I want the 
#print(ListArray[0]) just gives me the counts
ListType= data['type'].unique().tolist()
# this gives me the list of all types (some are not important) 
ListLen = [0]*len(ListType)

def MainCode():
	for i in range(RangeMaker()):
		d= {'Title': [data['title'].values[i]], 'Text': [data['text'].values[i]]}
		df = pd.DataFrame(data=d)
		count(data['type'].values[i])
		if ((str(data['type'].values[i]) == 'nan') or (len(str(data['type'].values[i]))>11) or (len(str(data['type'].values[i]))<2)):
			continue
		Filename= str(data['type'].values[i]) + str(ListLen[ListType.index(data['type'].values[i])]) #need to think about making this part.
		MyPath1 = os.path.join('/Applications','Smart Switch','AU ','Spring Semester 2019','Barouti independent study','Code for CSV','Put staff here', Filename)
		MyPath2= os.path.join(r'/Applications/Smart Switch/AU /Spring Semester 2019/Barouti independent study/Code for CSV/Put staff here'+'/'+ Filename)
		MYPath3 = os.path.join(MyPath2 +'/'+ Filename+ '.csv')
		# os.mkdir('/Applications/Smart Switch/AU /Spring Semester 2019/Barouti independent study/Code for CSV/Put staff here/Filename') 
		os.mkdir(MyPath1)
		df.to_csv(MYPath3)


def RangeMaker():
	Range = 0
	i=0
	for i in range(len(ListArray)):
		Range +=ListArray[i]
		i+=1
	return(Range) 


def count(n):
	for i in ListType:
		if (i==n):
			ListLen[ListType.index(i)]+=1
MainCode()
#print(ListArray)

#or (str(data['type'].values[i][0]== ['0','1','2','3','4','5','6','7','8','9'])) 
#Now I have problem because of all the NaNs in the system I dont get to all the folders I do need so I can increase the range from 12949 randomly to 20000 
#or I can write something that count the NaN or I can just sort the Excel before start working and then I dont even need the if (NaN) Part in the code.
# The end of the data is in 18008

# 1. make a one page report of the problems and what I found (BS issues): the range issue, the numbers issue, the types issue (all the noise)
# 2. try to fix BS problem .
# 3. check if bs is the only problem.
# 4. ideas how to solve the problems
# 5. add comments to the code and send it to Maria.
# We have 3 zeros and 1 of one.
# check if it correct for the whole process with putting the title and content
# I got read of the numbers but now I have another problem- I dont get State121 only until state120- fixed!!

# To make a csv file to compare the count and the index of the program (if there is a logical error).
