'''
Problem Statement:- You are given an array of integers arr[]. You have to reverse the given array.

'''

class Solution:
    def reverseArray(self, arr):
        # code here
        rev = arr[::-1]
        return rev


sol = Solution()

arr = [5,10,15,20,25]

result = sol.reverseArray(arr)

print("Reversed Array:", result)