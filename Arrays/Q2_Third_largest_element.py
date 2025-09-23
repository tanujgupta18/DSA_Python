'''
Question - https://www.geeksforgeeks.org/problems/third-largest-element/0

Problem Statement: Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.

'''

class Solution:
    def thirdLargest(self,arr):
        # code here
        n = len(arr)
        if (n<3):
            return -1
            
        first = second = third = float("-inf")
        
        for num in arr:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return third