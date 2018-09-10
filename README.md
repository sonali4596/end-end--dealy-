#END-TO-END-DELAY
SYNOPSIS:
end-to-end-delay1.py is a python program to compute end-to-end transmission in a network connecting Host
A to Host B via two routers R1,R2 using store and forward switching.

#HOW TO EXECUTE THE PROGRAM 
Program execution:

To execute the program, specify ./asn1.py and then give input as command line parameters.
THE PROGRAM TO BE INVOKED AS 

  python End-End-Delaylinks.py --t1 <value in Mbps> --t2 <value in Mbps> --t3< --d1 <value in KM> --d2 <value in KM> -N <value> -M <value in Mbits> -S <speed in 10^8m/s>
Example:

##INPUT:
C:\Users\sonali\Desktop>python end-to-end-delay.py --t1 10 --t2 20 --t3 10  --d1 5 --d2 6 --d3 7 -N 10 -M 20 -S 2 
   
####OUTPUT:
 Packet |   A   |------(   R   )----- (   R   )----------|   B  |
  P1      0.000         2000.050       3000.110           5000.180
  P2      2000.000      4000.050       5000.110           7000.180
  P3      4000.000      6000.050       7000.110           9000.180
  P4      6000.000      8000.050       9000.110           11000.180
  P5      8000.000      10000.050      11000.110          13000.180
  P6      10000.000     12000.050      13000.110          15000.180
  P7      12000.000     14000.050      15000.110          17000.180
  P8      14000.000     16000.050      17000.110          19000.180
  P9      16000.000     18000.050      19000.110          21000.180
  P10     18000.000     20000.050      21000.110          23000.180
 total delay: 140001.8
 
  ##PROBLEMS AND HOW I OVERCOME : 
 1)to write this program taking input before the running of the program I had to learn parsing of the command line arguments(tutorials    point )
 2) this program is written as we calculate the delay theoretically.
 3)the major problem was to calculate the queuing delay in STORE AND FORWARD APPROACH 
    OVERCOME
  a)I created the separate function delay1 and delay2 to calculate queueDelay1 and queueDelay2 separately .
  b) to calculate queuing delay I created a dequeue of maxsize 1. and the propagation delay  is taken as 1Mbps to calculate the queuing delay and propagation delay is ignored in doing final calculations.
  c)the queing delay is calculated as delay= [(propagation delay+transmission delay+processing delay)of previous packet  1] -[(propagation delay+transmission delay)of  packet 2]
  
    AND delay calculated is added with the R1 and R2 respectively .
    
    
    ###HOW THE PROGRAM WORKS 
    1)THE user enter the arguments while running the program 
    2)which is parsed by the getopt module 
    3)and  the values are assigned against to each variable 
    4)in while loop the delay is calculated and the output is displayed .
    
    ##### symbols used in program 
    A=SOURCE
      R1 =ROUTER1
      R2=ROUTER2
     B DESTINATION
 
