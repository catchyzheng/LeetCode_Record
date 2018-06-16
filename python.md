6/15 [561. Array Partition I](https://leetcode.com/problems/array-partition-i/description/)<br>
partition 2n number into n pairs, maximum the sum of the smaller one of each pair.<br>
```
def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum(sorted(nums)[::2])
```

[724. Find Pivot Index]()<br>

```
def pivotIndex(self, nums):
    # Time: O(n)
    # Space: O(1)
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1
```
