'''
Question - https://www.geeksforgeeks.org/problems/binary-search-1587115620/1

Problem Statement: 
Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. If k doesn't exist in arr[] return -1. 

Note: If multiple occurrences are there, please return the smallest index.

Approach:
1. Since the array is sorted, we can apply Binary Search to find the element efficiently.
2. Initialize two pointers: low = 0, high = len(arr) - 1.
3. Use a loop while low <= high:
   - Find the mid index.
   - If arr[mid] == k, store mid in result and search on the left side to find the first occurrence.
   - If arr[mid] < k, move to the right half (low = mid + 1).
   - If arr[mid] > k, move to the left half (high = mid - 1).
4. Return the value of result.
   - If k was found, result will have the first occurrence index.
   - If not found, result remains -1 and we return that.
'''
class Solution:
    def binarysearch(self, arr, k):
      # Code Here
      low = 0
      high = len(arr) - 1
      result = -1  
      
      while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            result = mid
            high = mid - 1  # Keep searching in the left half
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
      return result
      