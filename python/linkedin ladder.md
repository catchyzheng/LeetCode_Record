10.10 [364. Nested List Weight Sum II ](https://leetcode.com/problems/nested-list-weight-sum-ii/description/)  庆祝购买99元包年leetcode学生会员！

根节点权重为max_depth， 然后第i层节点权重max_depth - i （i从0开始）。求加权和。

和lintcode版本最大区别在于，这里传入函数的参数nestedList并不是一个NestedInteger实例，而是个list。list里面的元素才是NestedInteger。因此先要手动遍历一遍。

discuss里超级牛逼的思路，不用递归不用乘法。。[here](https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83641/No-depth-variable-no-multiplication)

```python
class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        deep = 0
        max_deep = 0
        def dfs(nlist):
            if nlist.isInteger(): return 1
            tmp_max = 0
            for ele in nlist.getList():
                tmp = 1 + dfs(ele)
                tmp_max = max(tmp, tmp_max)
            return tmp_max
        
        sum = 0
        def cal(depth, nlist):
            tmp_sum = 0
            if nlist.isInteger():
                return (max_deep - depth) * nlist.getInteger()
            
            for ele in nlist.getList():
                tmp_sum += cal(depth + 1, ele)
            return tmp_sum
        
        for list_ele in nestedList:
            max_deep = max(max_deep, dfs(list_ele))
        
        for list_ele in nestedList:
            sum += cal(0, list_ele)
        
        return sum
```



以下为lintcode。

10.9 [94. Binary Tree Maximum Path Sum](https://www.lintcode.com/problem/binary-tree-maximum-path-sum/description)

累死我了。。。还超时30分钟。。medium。

注意：可以是一个节点，可以从任意节点开始结束。

```python
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    max_ = float('-inf')
    def maxPathSum(self, root):
        # write your code here
        if not root: return 0
        def dfs(node):
            if node is None: return 0
            sum_ = 0
            if self.max_ < node.val: self.max_ = node.val
            left = right = 0
            if node.left is not None: left = dfs(node.left)
            if node.right is not None: right = dfs(node.right)
            
            sum_ = node.val + (left if left > 0 else 0 ) + (right if right > 0 else 0)
            if self.max_ < sum_: self.max_ = sum_
            if left < 0 and right < 0:
                return node.val
            else: 
            return node.val + (left if left > right else right)
        ans = dfs(root)
        
        return self.max_
```

如果左右子树都路径和小于0， 那就不如直接返回节点本身了。



10.8 [30. Insert Interval ](https://www.lintcode.com/problem/insert-interval/description?_from=ladder&&fromId=23)

惊呆了。。leet上面hard的题竟然在这里是easy。

但，下面这个代码的思路是真的巧妙！代码量少而且很巧妙啊。

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        l, r, s, e = [], [], newInterval.start, newInterval.end
        for ele in intervals:
            if ele.end < s:
                l += ele,
            elif ele.start > e:
                r += ele,
            else:
                s = min(s, ele.start)
                e = max(e, ele.end)
        return l + [Interval(s, e)] + r
```



10.8 [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

别人家的短小精悍的代码。。值得学习

```python
def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
```

10.8 [165. Merge Two Sorted Lists ]()

注意判空。

10.8 [156. Merge Intervals](https://www.lintcode.com/problem/merge-intervals/description?_from=ladder&&fromId=23)

重点在排序！记住这个python3 的通用自定义排序写法，sorted， key。

如果是元组排序，可以参看[这个链接](https://docs.python.org/3/howto/sorting.html)

使用itemgetter和attrgetter直接指定列号或者属性，按优先级排序。

```python
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        def compare(elem):
            return elem.start
            
        res = []
        intervals = sorted(intervals, key = compare)
        
        for inter in intervals:
            if len(res) == 0: res.append(inter)
            else:
                if inter.start <= res[-1].end:
                    res[-1].end = max(res[-1].end, inter.end)
                else:
                    res.append(inter)
        return res

```

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

