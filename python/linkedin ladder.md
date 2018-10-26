10.20 [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/)

给定一个value，找到BST中最近的K个值。

其实，如果可以新建数组的话， 那和270很像。inorder遍历生成有序列表后bisect.bisect找到要插入的位置，然后双指针往前往后遍历找到k个。

但，如果不给新建，而且是平衡树时候，要求logn复杂度，那就得想新办法了。。。

听说有最优解？[here](https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70503/O(logN)-Java-Solution-with-two-stacks-following-hint?page=1)

10.20 [270. Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/description/)（这只是简化版本。寻找K个才是难）

给定一个value，找到BST中最近的值。

转换成列表然后二分很容易想到。但如果不能转换二分，只能在树中查找呢？

```python
class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        if not root: return None
        
        minDist = float('+inf')
        res = None
        
        while root:
            dist = abs(root.val - target)
            if dist < minDist:
                minDist = dist
                res = root.val
            
            if target > root.val:
                root = root.right
            elif target < root.val:
                root = root.left
            else:
                break            
            
        return res
```

方法是，如果value比当前node的值大，那就和右节点继续比较。如果小，就和左节点。否则直接返回。



10.20 [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/)

tradeoff between quick add and quick find. 



10.20 [244. Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/description/)

Design a class which receives a list of words in the constructor, and implements a method that takes two words *word1* and *word2* and return the shortest distance between these two words in the list. Your method will be called ***repeatedly*** many times with different parameters. 

**Example:**
Assume that words = `["practice", "makes", "perfect", "coding", "makes"]`.

```
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
```

**Note:**
You may assume that *word1* **does not equal to** *word2*, and *word1* and *word2* are both in the list.

坑点：不要妄想所有工作在init中做完。

```python
import collections
class WordDistance:
    vector = collections.defaultdict(list)
    #hashmap = dict()
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.vector.clear()
        for i in range(len(words)):
            self.vector[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p, q = 0, 0
        min_dist = float('inf')
        while p < len(self.vector[word1]) and q < len(self.vector[word2]):
            if self.vector[word1][p] <= self.vector[word2][q]:
                min_dist = min(min_dist, self.vector[word2][q] - self.vector[word1][p])
                p += 1
            else:
                min_dist = min(min_dist, self.vector[word1][p] - self.vector[word2][q])
                q += 1
        return min_dist
    
    '''
    v = collections.defaultdict(list)
    v[4].append('fuck')
    v[2].append('ass')
    for k in v.keys():
        print(k, v[k])    
    '''
```

思路不难， 就是记录下每个单词的所有出现位置index存为列表。然后每次要查询时候，就双指针遍历两列表。每次移动在words中index更小的下标指针。



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



**以下为lintcode。**

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

