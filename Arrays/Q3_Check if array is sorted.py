'''
Question - https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/0

Problem Statement: Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.


'''
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True