8/4 [31. Next Permutation](https://leetcode.com/problems/next-permutation/description/)

题意：给出一个排列，修改成字典序的下一个排列。。

看了解答思路后自己写出来的代码。

```python
    def nextPermutation(self, nums):
        """
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        index = -1
        for i in range(size-1, 0, -1):
            if nums[i-1] < nums[i]:
                index = i-1; break
        if index == -1: 
            nums.reverse(); return
        for i in range(index+1, size):
            if nums[i] >= nums[index]:
                if i+1 == size or (i+1 < size and nums[i+1] <= nums[index]):
                    nums[i], nums[index] = nums[index], nums[i]; break
        i, j = index+1, size-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1; j -= 1
        return
```

基本思路：从后往前，找到第一个a[i]<a[i+1]的i。

然后再在i右边找到一个下标j，使得a[i]<=a[j] 且 a[i]>=a[j+1]，交换a[i] a[j]

然后将i右边部分反转。注意一些边界情况。