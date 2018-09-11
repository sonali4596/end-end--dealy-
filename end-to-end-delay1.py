import sys			#this module is imported to  use command line arguments  
import getopt		# this module is imported  to parse the command  line arguments 
from collections import deque
def transDelay(t,M):		#calculating transmission delay  [Transmission Delay = Data size / bandwidth = (M/t) second]
	return (float(M)*1024/t*10**6)

def propDelay(d): 		# calculation propagation delay  [Propagation delay = distance/transmission speed = d/S]
	return d/(2*100.00**5)

def main():  		# MAIN FUNCTION STARTS HERE 
	t1,t2,t3,d1,d2,d3,N,M = 1,1,1,1,1,1,1,1, #Default values  when the value for a particular is not entered  it will not work if no value is entered 
	try:			# exception handling used incase to check wether user has input the arguments  or not 
		opts, args = getopt.getopt(sys.argv[1:],'N:M:p:',['t1=','t2=','t3=','d1=','d2=','d3=','help'])#long and short options for parsing the arguments 
	except getopt.GetoptError as err: 		#exception  when argument is passed zero or  wrong  and existing the system
			print (err)
			print ("Please use the correct arguments, for usage type --help ")
			sys.exit(2)

	for opt,arg in opts:		# taking argumnts  one by one from opts and assigning it to  respective options  using nested if-else
		
		
		if opt == '--t1':
			t1 = float(arg)
		elif opt == '--t2':
			t2 = float(arg)
		elif opt == '--t3':
			t3 = float(arg)
		elif opt == '--d3':
			d3 = float(arg)
		elif opt == '--d1':
			d1 = float(arg)
		elif opt == '--d2':
			d2 =float(arg)
		elif opt == '-N':
			N = float(arg)
		elif opt == '-M':
			M = float(arg)
		elif opt == '--help':
			printHelp()
		else:
			assert False, "unhandled option" 		#assertion  error is raised  if the entered argument is  does not match with the parsed options
	print ('%10s%5s%9s%20s%9s%20s%9s%20s%9s' % ("Packet  "," ","|   A   |","-" * 20,"(   R   )","-" * 20,"(   R   )","-" * 20,"|   B   |"))
	
	n,A,queueDelay1,queueDelay2,c= 1,0,0,0,0		#the variables used for calcualtion of delay 
	while n<=N: 			#calculation of delay  where "A" is source  AND DESTINATION IS "B"
		
		R1 = A + transDelay(t1,M) + propDelay(d1)#calculating  the delay  at router one  which is denoted at "R1"
		R2 = R1 + queueDelay1 + transDelay(t2,M) + propDelay(d2)		#calculating  the delay  at router two  which is denoted as "R2"
		B = R2 + queueDelay2 + transDelay(t3,M) + propDelay(d3)		#calculating  the  delay at router destination "B"
		c=c+B
		queueDelay1=queue1(t1,M,d1,n)
		queueDelay2=queue2(t2,M,d2,n)
		
		
		#if R1 < transDelay(t2,M):
			#queueDelay1 = queueDelay1 + transDelay(t2,M) - transDelay(t1,M)
		#if R2 < transDelay(t3,M):#  
			#queueDelay2 = queueDelay2 + transDelay(t3,M) - transDelay(t2,M)
		print('%10s%5s%9.3f%20s%9.3f%20s%9.3f%20s%9.3f' % ('P' + str(n) + '    ','',A,'',R1,'',R2,'',B))
		n,A = n + 1,A + transDelay(t1,M) #incrementing of n and "A" is done here 
	print("total delay:",c)
	print ("-----------------------------------------------------------------------------------------------------------------")
		
def printHelp():
	print ("We have multiple options:\n\t 1:--t1: Transmission Delay at Link1 <value in Mbps>\n\
			2:--t2: Transmission Delay at Link2 <value in Mbps>\n\t
			3:--t3: Transmission Delay at Link3 <value in Mbps>\n\
			4:--d1: Distance of Link1<value in KM>\n\t
			5:--d2: Distance of Link2 <value in KM>\n\t
			6:--d3: Distance of Link3 <value in KM>\n\
			7:-N: Number of Packets <value>\n\t 
	       		8:-M: Packet Size <value in kbits>)
	sys.exit()
def queue1(t1,M,d1,n):#calculating queing delay for router one assuming that no packet is in the queue when other is processing 
	pkt=list()
	q = deque( maxlen=1 )
	p=10**6
	if n==1:
		s1=packet1(t1,d1,M)
		r1=s1+(M/p)
		
	else:
		q.append(pkt[n])
		q1=packet1(t1,d1,M)
		delay=r1-q1
		q.pop(pkt[n])
	return delay
def queue2(t2,M,d2,n):#calculating queing delay for router two that no packet is in the queue
	pkt=list()
	q = deque( maxlen=1 )
	p=10**6
	if n==1:
		s2=packet10(t2,d2,M)
		r2=s2+(M/p)
		
	else:
		q.append(pkt[n])
		q2=packet10(t1,d1,M)
		delay=r2-q2
		q.pop(pkt[n])
	return delay
	
def packet1(t1,d1,M):
	p1 = transDelay(t1,M) + propDelay(d1)#calculating  the delay  at router one  which is denoted at "R1"
	return p1
def packet10(t2,d2,M):
	p2 = transDelay(t2,M) + propDelay(d2)		#calculating  the delay  at router two  which is denoted as "R2"
	return p2
if __name__ =='__main__':
        main()
