10.26 [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)



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



10.26 [582. Kill Process](https://leetcode.com/problems/kill-process/description/)



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

