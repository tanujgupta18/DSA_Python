'''
Question - https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

Problem Statement: 
Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

Note: You can return the elements in any order but the driver code will print them in sorted order.

Approach:
1. Since the elements are from 1 to n and can appear at most twice, we can use a hash map (dictionary) to count occurrences.
2. Traverse the array once and count the frequency of each number.
3. Traverse the hash map to collect all numbers that appeared exactly twice.
4. Return the list of duplicates (the driver code will sort it).

'''

class Solution:
    def findDuplicates(self, arr):
        # code here
        count = {}
        result = []
        
        for num in arr:
            count[num] = count.get(num,0) + 1
        
        for num in count:
            if count[num] == 2:
                result.append(num)
        
        return sorted(result)