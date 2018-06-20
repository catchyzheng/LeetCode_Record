6/18 [climbing stairs]
```
def climbStairs2(self, n):
    # write your code here
    if(n==0||n==1): return 1
    if(n==2): return 2
    if(n==3): return 4
    p = [1,2,4]
    for i in range(3,n):
        p.append(p[-1]+p[-2]+p[-3]) //hao hao!!
    return p[-1]
```

6/18 [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)<br>
牛逼的不行。。。
```
def groupAnagrams(self, strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()
```

6/18 [720. Longest Word in Dictionary]()<br>

```
def longestWord(self, words):
    ans = ""
    wordset = set(words)
    for word in words:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                ans = word

    return ans
```

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



