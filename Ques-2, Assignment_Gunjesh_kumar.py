#!/usr/bin/env python
# coding: utf-8

# In[5]:


def is_prime(number):
    if number==1:
        return False
    
    #Debugged here: changed start of range function and an operator below.
    
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def find_prime_numbers(start,end):
    prime_numbers=[]
    for num in range(start,end+1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


# In[6]:


start_range=1
end_range=50
expected_primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
result=find_prime_numbers(start_range,end_range)

if result==expected_primes:
    print("Congratulations! The function is correct")
else:
    print("Too bad! There is some bug in the function.")

Debugging involved two changes:
    1. Changed the start of range function to 2 from 1. This is because a prime number is always divisible by 1.
    2. Chnaged the operator from "/" to "%". This is because the quotient(given by "%") upon dividing the 'number' by 'i' should        be Zero.
   
# In[ ]:




