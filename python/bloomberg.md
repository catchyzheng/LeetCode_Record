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



10.28 []

given a maze, 0 is ground, 1 is wall, -1 is treasure. You need to find how many treasure can be reached.

1是墙。就是一个dfs找所有可达-1.

```python
class Solution(object):
    def hasPath(self):
    	maze = [[ 0, 0,-1, 0, 0],\
                [ 1, 1, 0, 0, 1],\
                [ 0, 1,-1, 0,-1],\
                [-1, 1, 0, 0, 1],\
                [-1, 1,-1, 0, 0]]
        
        m = len(maze); n = len(maze[0])
        visit = [[0 for _ in range(n)] for __ in range(m)]
        start = [0, 0]
        self.cnt = 0
        treasure = []
        def dfs(maze, sx, sy):
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            
            for d in dirs:
                x = sx+d[0]; y = sy + d[1]
                if x>=0 and x<m and y>=0 and y<n and maze[x][y]!=1 and visit[x][y]==0:
                    visit[x][y] = 1
                    if maze[x][y]==-1: 
                        self.cnt += 1
                        treasure.append([x, y])
                    dfs(maze, x, y)
        visit[start[0]][start[1]] = 1
        dfs(maze, start[0], start[1])
        
        print(self.cnt)
```



10.27 [505. The Maze II](https://leetcode.com/problems/the-maze-ii/description/)

this is not from bloomberg but it is good to put here. 提醒自己多熟悉图和路径相关的题目。

给定一个矩阵，0表示空地1表示墙。给定球的位置和洞口位置，都在空地上。球会沿着一个方向一直滚直到遇到墙或者边界。问**最短路径是多少，并输出**。maze3是问依次输出球滚动的方向。大不了每次计算两个相邻路径点之间的相对位置，然后返回方向。

还没看dijstra算法怎么做的。。。。

```python
class Solution(object):
    def shortestDistance(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        dist = [[float('inf') for _ in range(n)] for __ in range(m)]
        dist[start[0]][start[1]] = 0
        pre = [[ [-1, -1] for _ in range(n)] for __ in range(m)]
        action = [[ '0' for _ in range(n)] for __ in range(m)]
        self.dfs(maze, start, dist, pre, action)
        for i in range(m):
            for j in range(n):
                print dist[i][j],
            print ''
        if dist[dest[0]][dest[1]] == float('inf'):
            return -1
        else: 
            xx, yy = dest[0], dest[1]
            print [xx, yy]
            while [xx, yy] != start:
                # print the path
                print pre[xx][yy]
                [xx, yy] = pre[xx][yy]
                # should not xx = pre[xx][yy][0]; yy = pre[xx][yy][1] !!!
            return dist[dest[0]][dest[1]]
        
    def dfs(self, maze, start, dist, pre, action):
        dirs = [[-1,0], [1,0], [0, -1], [0,1]]
        hmap = ['u', 'd', 'r', 'l']
        i = 0
        for d in dirs:
            i += 1
            x = start[0] + d[0]
            y = start[1] + d[1]
            cnt = 0
            # while means each time the ball move continuely until reach wall. if means each time move one step.
            while x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]!=1:
                x += d[0]; y += d[1]
                cnt += 1
            if dist[x-d[0]][y-d[1]] > dist[start[0]][start[1]] + cnt:
                dist[x-d[0]][y-d[1]] = dist[start[0]][start[1]] + cnt
                pre[x-d[0]][y-d[1]] = [start[0], start[1]]
                action[x-d[0]][y-d[1]] = hmap[i%4]
                #print pre[x-d[0]][y-d[1]]
                self.dfs(maze, [x-d[0], y-d[1]], dist, pre, action)
        
```



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

