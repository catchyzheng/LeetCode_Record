10.28 [47. Permutations II](https://leetcode.com/problems/permutations-ii/description/)

give a list that contains duplicates, return all its permutation. 

普通回溯。注意如何判断语句去重。

```python
import copy
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmplist = [] # store every result
        res = [] # store all results
        l = len(nums)
        visit = [False for _ in range(l)]
        def dfs(cnt):
            if cnt==l:
                res.append(copy.copy(tmplist))
                return
            for i in range(0, l):
                if visit[i] or i > 0 and nums[i] == nums[i-1] and not visit[i-1]: 
                    continue
                if not visit[i]:
                    visit[i] = True
                    tmplist.append(nums[i])
                    dfs(cnt+1)
                    visit[i] = False
                    tmplist.pop()
            
            
        nums.sort()
        dfs(0)
        return res
```

注意！当num长度1时候，i=0，num[i] == num[i-1]是真的，就是自己。



10.28 [90. Subsets II](https://leetcode.com/problems/subsets-ii/description/)

Given a collections that contains duplicates, find all its subsets. 

以下代码来自排行榜，让你见识下除了典型递归回溯外的更巧妙解法。完美利用了子集的特点。

```python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        ans = [[]]
        cur = []
        for i in range(len(S)):
            if i == 0 or S[i] != S[i-1]:
                cur = [item + [S[i]] for item in ans]
            else:
                cur = [item + [S[i]] for item in cur]
            ans += cur
        return ans
```





10.28 [401. Binary Watch](https://leetcode.com/problems/binary-watch/description/)

not solved, yet is easy. 





10.28 [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)



```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        l = len(digits)
        res = []
        final = []
        def dfs(i):
            if i == l:
                if len(res) > 0: final.append(''.join(res))
                return
            for x in char[int(digits[i])]:
                res.append(x)
                dfs(i+1)
                res.pop()
        dfs(0)
        return final
```

