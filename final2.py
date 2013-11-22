#!/usr/local/bin/python3
"""final project """
import sys

def plot(freq):
	
	step = 20
	
	xax = max(freq.keys()) + 1
	yax = max(freq.values()) + 200
	 
	
	for j in range(yax,-1,-step):
		if j%100  < step:
			sym = "{0:>3}{1:>3}".format(j, "-|")
		else:
			sym = "{0:>3}{1:>3}".format(" ", "|")	
			
		for i in range(1, xax):
		 	if i in freq.keys() and freq[i] >= j:
		 		sym += 	"***"
		 	else:
		 		sym += " "		 							 							
			
		print(sym)

	sym= "{0:>4}".format("-+--")
	for i in range(1,xax):    	
        	sym += "+--"
	print(sym)

	indexing = "    "
	for i in range(1, xax):
		indexing += "{0:>3}".format(i)
	print(indexing)
    			
if __name__ == "__main__":		

	try:
		f=open(sys.argv[1],'r')
		text = f.read()
		lenfreq = {}  #lengths occurance
		for punc in ",?;.&:-'":
			text = text.replace(punc,"")

		print('Length','Count')

		for word in text.split():
			k = len(word)
			if k in lenfreq:
				lenfreq[k] +=1
			else:
				lenfreq[k] =1
			
		for leng in sorted(lenfreq.keys()):
			print(leng,lenfreq[leng])				
		f.close()

		plot(lenfreq)
	
	
	except IndexError:
		print('Please enter the file name')

	except IOError:
 		print('File not found')	