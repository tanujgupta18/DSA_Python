'''
Question - https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

Problem Statement: 
You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Approach:
The sum of the first n natural numbers is given by the formula: n * (n + 1) // 2.
By subtracting the sum of the given array from this expected total sum, we get the missing number.


'''
class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        total_sum = n * (n+1) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum