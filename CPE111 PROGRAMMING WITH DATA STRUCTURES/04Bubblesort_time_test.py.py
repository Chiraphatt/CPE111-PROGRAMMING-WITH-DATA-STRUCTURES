#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
import time
import matplotlib.pyplot as plt

# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theSeq ):
    n = len( theSeq ) - 1
    # Perform n-1 bubble operations on the sequence
    for i in range( n , 0 , -1 ) :
        # Bubble the largest item to the end.
        for j in range(i) :
            if theSeq[j] > theSeq[j + 1] : # swap the j and j+1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq

num = [100, 200,400,500,600,700,800,900,1000,2000,4000,5000,6000,7000,8000,9000,10000]
Average = []
Best = []
Worst = []
for j in num :
    seq = [] 
    for i in range(0 , j ):
        seq.append(random.randint( 1, j ))
        
    start_A = time.time( )
    A = bubbleSort(seq)
    end_A = time.time( )
    elapsed_A = end_A - start_A
    
    Average.append(elapsed_A)
    
    start_B = time.time( )
    B = bubbleSort(A)
    end_B = time.time( )
    elapsed_B = end_B - start_B
    
    Best.append(elapsed_B)

    B_reversed = reversed(B)
    start_W = time.time( )
    W = bubbleSort(list(B_reversed))
    end_W = time.time( )
    elapsed_W = end_W - start_W
    
    Worst.append(elapsed_W)
    
print("Green is Average Case")
print("Blue is Best Case")
print("Red is Worst Case")

plt.title('Bubble Sort', fontsize = 25)
plt.xlabel("number of sequence")
plt.ylabel("Time")
plt.plot(num, Average,'g',num, Best,'b',num, Worst,'r')

plt.show()


# In[ ]:





# In[ ]:




