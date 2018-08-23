8/22 [960. First Unique Number in a Stream II](https://www.lintcode.com/problem/first-unique-number-in-a-stream-ii/description)

不断读取数字，实时返回第一个独特数字。 

```python
class DataStream:
    
    def __init__(self):
        # do intialization if necessary
        self.counter = collections.defaultdict(int)
        self.queue = collections.deque()
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if self.counter[num] > 1:
            return

        if self.counter[num] == 0:
            self.queue.append(num)
        self.counter[num] += 1

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        while self.queue and self.counter[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0]
```



8/22 [685. 数据流中第一个唯一的数字 ](https://www.lintcode.com/problem/first-unique-number-in-stream/description)

给一个连续的数据流,写一个函数返回终止数字到达时的第一个唯一数字（包括终止数字）,如果在终止数字前无唯一数字或者找不到这个终止数字, 返回-1.

思路不难，用dict就行。但有坑。坑在哪？找找margin case。

```python
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        dict = {}
        list = []
        isbreak = False
        for num in nums:
            if dict.has_key(num):
                dict[num] += 1
            else: 
                list.append(num)
                dict.setdefault(num, 1)
            
            if num == number: 
                isbreak = True; break
        
        if not isbreak: return -1
        for key in list:
            if dict.get(key) == 1: return key
        
        return -1

```

一，要求第一个出现一次的数字，而dict中是按照key大小排序的。

二，可能数组中不包含终止数字。