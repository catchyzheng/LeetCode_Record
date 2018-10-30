



10.28 [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)



10.28 [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

找最近公共祖先。自己可以算自己的祖先。 注意是找最近不是最远。

用了好多临时变量的空间。。

自己的基本想法就是构建一个parent数组，由子女指向父母。然后从p往上遍历直到root。 q开始往上遍历，如果出现在p路径上就返回。

discuss貌似有个很巧妙的递归方法。

```python
from collections import defaultdict
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        hmap = defaultdict(TreeNode)
        hmap[root] = root
        self.dfs(hmap, root, root)
        
        lst_p = [p]
        while p.val != hmap[p].val:
            lst_p.append(hmap[p])
            p = hmap[p]
        if q in lst_p: return q
        lst_q = [q]
        while q.val != hmap[q].val:
            if hmap[q] in lst_p: return hmap[q]
            lst_q.append(hmap[q])
            q = hmap[q]
        
        
    def dfs(self, hmap, node, parent):
        hmap[node] = parent
        parent = node
        if node.left is not None: self.dfs(hmap, node.left, parent)
        if node.right is not None: self.dfs(hmap, node.right, parent)
        return
        
```



First question: Initially I was given a number that I should consider as terminating number. Given a continuous stream of numbers, write a function that returns the first unique number whenever terminating number is reached. Interviewer wanted an answer that was in O(1) when a terminating number is reached, so basically preprocessing was required.
Through this question, my knowledge on how process works, I mean what is heap. stack, global variables, local variables was also checked. i was also asked how hash map works, its time complexity, how it is calculated, I was also asked in detail about linked list and array and also about iterator dereference.

Apart form this, I was also about my most challenging project, most boring project, why I chose Computer Science as my field, why Bloomberg etc

10.28 [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/description/)

链表的表头变成了数字的最高位。

```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

解法： 1 存入stack变成逆序 2 直接遍历转成数字相加。

10.28 [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

链表**经典题**，链表头是个位。几个注意 事项，自己先想想。		

```python
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        p1 = l1; p2 = l2
        sign = 0
        pre = ListNode(-1)
        start = pre
        while p1 is not None or p2 is not None:
            x = 0 if p1 is None else p1.val # 这个方法好！
            y = 0 if p2 is None else p2.val    
            sum_ = (x + y + sign) % 10
            sign = int((x + y + sign)/10)
            cur = ListNode(sum_)
            pre.next = cur
            pre = pre.next
            if p1 is not None: p1 = p1.next
            if p2 is not None: p2 = p2.next
            
        if sign > 0:
            last = ListNode(sign)
            pre.next = last
        return start.next
```

1 空链表 2 长度不一样 3 1+99





10.27 [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/description/)

```python
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)
        print 'init: ', 
        for x in self.stack:
            print x.val,
        print ''
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        print tmpNode.val
        print 'next, before push all: ', 
        for x in self.stack:
            print x.val,
        print ''
        
        self.pushAll(tmpNode.right)
        
        print 'next, after push all: ', 
        for x in self.stack:
            print x.val, 
        print ''
        return tmpNode.val
        
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
    
    '''def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lst = []
        def dfs(root):
            if root.left is None and root.right is None: 
                self.lst.append(root.val); return 
            if root.left is not None: dfs(root.left)
            self.lst.append(root.val)
            if root.right is not None: dfs(root.right)
            return
        if root is not None: dfs(root)
        self.l = len(self.lst)
        self.cur = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur < self.l:
            #self.cur += 1
            return True
        return False
        

    def next(self):
        """
        :rtype: int
        """
        index = self.cur
        self.cur += 1
        return self.lst[index]'''
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
```





10.26 [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)

要求，什么操作都是常数时间复杂度。那必然是要增大空间重复存储元素了。怎么存？

```python
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vec = []
        self.pos = {}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.pos[val] = len(self.vec)
            self.vec.append(val)
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            remove_index = self.pos[val]
            self.pos[self.vec[-1]] = remove_index
            del self.pos[val]
            
            self.vec[remove_index], self.vec[-1] = self.vec[-1], self.vec[remove_index]
            self.vec.pop()
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        l = len(self.vec)
        index = random.randint(0, l-1)
        return self.vec[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

一个list存当前已有的所有不重复元素。一个dict存元素和对应的下标。

注意，delete指定元素时候，要交换该指定元素和list末尾元素，以及对应下标，以便直接pop，达到常数时间。

10.26 [582. Kill Process](https://leetcode.com/problems/kill-process/description/)

简单。遍历指定节点对应的子树就行。

```python
from collections import defaultdict
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        child = defaultdict(list)
        
        for son, par in zip(pid, ppid):
            if par != 0:
                child[par].append(son)
        '''
        l = len(pid)
        for i in range(l):
            if ppid[i] != 0:
                child[ppid[i]].append(pid[i])
        
        res = [kill]
        tmp = [kill]
        while len(tmp) > 0:
            top = tmp.pop(0)
            tmp.extend(child[top])
            res.extend(child[top])
        '''
        res = [kill]
        i = 0
        while i < len(res):
            if res[i] in child.keys():
                res.extend(child[res[i]])
            i+= 1
               
        return res
        
```

