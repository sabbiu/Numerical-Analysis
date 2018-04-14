'''
KAHAN ALGORITHM
----------------
https://en.wikipedia.org/wiki/Kahan_summation_algorithm

Relies on the fact that,
(((a + b) - a) - b) != 0

We must store compensation value and
add it back at every summation

Explanation: When we add much larger number with smaller number
then, we loose the precision of lower digits in smaller number.
Thus, on every new sum, we add previous lost compensation.
'''

import numpy as np
kahanSum, compensation, naiveSum, size = 0, 0, 0, 100000000

nums = np.zeros(size)
perms = np.random.permutation(size)

for i in range(size):
    nums[perms[i]] = i / 13

for i in range(len(nums)):
    num = nums[i]

    # # Kahan Algorithm
    # take new number and add previous compensation to it
    nextTerm = num + compensation
    # add compensated number with the sum
    nextSum = kahanSum + nextTerm
    # calculate the compensation value
    # to be used in next step of calculation
    compensation = nextTerm - (nextSum - kahanSum)
    # final rounded sum
    # Question : Why round it? Why not store all the value?
    # Answer: B/c of the limitation of the bit storage,
    # we cannot store all the bits. So, least digit are rounded off.
    kahanSum = nextSum

    # # Naive Sum
    naiveSum += num

print ("Kahan Sum: %.5f\nNaive Sum: %.5f" %(kahanSum, naiveSum))
