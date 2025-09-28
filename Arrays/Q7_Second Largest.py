'''
Question - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

Problem Statement: 
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Approach:
1. If the array has less than 2 elements, return -1.
2. Initialize two variables:
   - first = -∞ (to store the largest)
   - second = -∞ (to store the second largest)
3. Traverse the array:
   - If current number > first:
       - second = first
       - first = current number
   - Else if current number > second and not equal to first:
       - second = current number
4. Return second if valid, else -1.

'''
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        if n < 2:
            return -1
            
        first = second = float("-inf")
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        
        if second == float("-inf"):
            return -1
            
        else:
            return second
