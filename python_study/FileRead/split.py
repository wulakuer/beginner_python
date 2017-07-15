import os
data=open('sketch.txt')
data.seek(0)
data.tell()
for each_line in data:
	if not each_line.find(':')==-1:
		(actor,sentence)=each_line.split(':',1)
		print(actor,end='')
		print(sentence, end='')
	else:
		print(each_line,end='')
data.close()
