'''
Question - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

Problem Statement: 
You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Approach:
1. We’re just using a variable pos to track where to put the next non-zero element.
2. First loop: go through the array, whenever you find a non-zero, put it at arr[pos] and move pos forward.
3. Second loop: once all non-zeroes are placed, fill the rest of the array with 0s from pos till the end.

'''
class Solution:
    def pushZerosToEnd(self, arr):
        l = len(arr)
        pos = 0

        for i in range(l):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1

        while pos < l:
            arr[pos] = 0
            pos += 1