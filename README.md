#END-TO-END-DELAY
SYNOPSIS:
end-end--delay.py is a python program to compute end-to-end transmission in a network connecting Host
A to Host B to Host C via two routers R1,R2 using store and forward switching.

#HOW TO EXECUTE THE PROGRAM 
Program execution:

To execute the program, specify ./asn1.py and then give input as command line parameters.

The program is to be invoked as

  python End-End-Delaylinks.py --t1 <value in Mbps> --t2 <value in Mbps> --d1 <value in KM> --d2 <value in KM> -N <value> -M <value in Mbits> -S <speed in 10^8m/s>
Example:

Input:
C:\Users\sonali\Desktop>python end-to-end-delay.py --t1 10 --t2 20 --t3 10  --d1 5 --d2 6 --d3 7 -N 10 -M 20 -S 2 
   
Output:
 Packet      |   A   |--------------------(   R   )--------------------(   R   )--------------------|   B  |
 P1             0.000                       2000.025                     3000.055                     5000.090 
 P2             2000.000                    4000.025                     5000.055                     7000.090
 P3             4000.000                    6000.025                     7000.055                     9000.090
 P4             6000.000                    8000.025                     9000.055                     11000.090
 P5             8000.000                    10000.025                    11000.055                    13000.090	
 P6             10000.000                   12000.025                    13000.055                    15000.090
 P7             12000.000                   14000.025                    15000.055                    17000.090
 P8             14000.000                   16000.025                    17000.055                    19000.090
 P9             16000.000                   18000.025                    19000.055                    21000.090
 P10            18000.000                   20000.025                    21000.055                    23000.090
 total delay: 140000.9
 
 problems overcome 
 1)to write this program taking input before the running of the program I had to learn parsing of the command line arguments(tutorials point )
 2) this program is written as we calculate the delay theoretically.
 
