#!/usr/bin/env python
# coding: utf-8

# In[1]:


def two_sum_closest(nums, target):
    closest_sum = float('inf')  # Initialize to positive infinity
    result = None

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            current_sum = nums[i] + nums[mid]

            # Check if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                result = (nums[i], nums[mid])

            elif current_sum < target:
                left = mid + 1
            else:
                right = mid - 1

    return result

# Example usage:
sorted_array = [-2, 0, 1, 2, 3]
target = 0
result = two_sum_closest(sorted_array, target)
print(result)  


# In[2]:


def max_profit(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
            i = i+2

    return max_profit

# Test case

print(max_profit([1, 2, 3, 4, 5])) 


# In[4]:


from math import sqrt

# Function check whether a number is prime

def isPrime(n):
    
    if (n<=1):
        return False
    
    for i in range(2, int(sqrt(n)+1)):
        if (n%i==0):
            return False
    return True

    

def find_first_100_twin_primes():
    twin_primes = []
    num = 3  # Start checking from the first possible twin prime pair (3, 5)

    while len(twin_primes) < 100:
        if isPrime(num) and isPrime(num + 2):
            twin_primes.append((num, num + 2))
        num += 2  # Move to the next odd number

    return twin_primes

# Example usage:
first_100_twin_primes = find_first_100_twin_primes()
for pair in first_100_twin_primes:
    print(pair)


# In[ ]:


K=0;
for i in range(n//2,n):
    for j in range(2,,n,pow(2,j)):
        k=k+n/2


# The time complexity of the provided code is  O(n * log2(n)).
# 
# The outer loop iterates from n // 2 to n, which is roughly half the size of n. So, it runs approximately n // 2 times.
# 
# The inner loop starts at 2 and doubles j in each iteration until j reaches or exceeds n. This effectively makes the inner loop run approximately log2(n) times.
# 
# Inside the inner loop, there are constant-time operations such as addition and division.
# 
# In summary, the time complexity of the code can be approximated as O((n // 2) * log2(n)), which simplifies to O(n * log2(n)) in big O notation.

# In[ ]:


value=0
for i in range(n):
    for j in range(i):
        value=value+1


# The time complexity of the provided code is O(n^2).
# 
# The provided code has nested loops. The outer loop iterates 'n' times, and for each iteration of the outer loop, the inner loop runs an average of 'n/2' times. Inside the inner loop, there are constant-time operations.
# 
# As a result, the overall time complexity of the code is O(n * (n/2)), which simplifies to O(n^2) in big O notation.
