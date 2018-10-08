10.8 [551. Nested List Weight Sum](https://www.lintcode.com/problem/nested-list-weight-sum/description?_from=ladder&&fromId=23)

Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Given the list `[[1,1],2,[1,1]]`, return `10`. (four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
Given the list `[1,[4,[6]]]`, return `27`. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)

```python
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        def dfs(deep, nestedList):
            sum = 0
            for ele in nestedList:
                if ele.isInteger():
                    sum += deep * ele.getInteger()
                else:
                    sum += dfs(deep + 1, ele.getList())
            return sum
        deep = 1
        
        return dfs(1, nestedList)

```

