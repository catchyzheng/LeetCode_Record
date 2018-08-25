8/25 [81. 数据流中位数](https://www.lintcode.com/problem/find-median-from-data-stream/description)

好巧妙的方法。。。都不需要实时存放当前中位数用于和新来的数比较。

```java
PriorityQueue<Integer> min = new PriorityQueue();
PriorityQueue<Integer> max = new PriorityQueue(1000, Collections.reverseOrder());
//当JDK8的时候，可以直接写成，不再需要初始化容量
//PriorityQueue<Integer> max = new PriorityQueue(Collections.reverseOrder());
 
public void Insert(Integer num) {
    max.offer(num);
    min.offer(max.poll());
    if (max.size() < min.size()) {
        max.offer(min.poll());
    }
}
 
public Double GetMedian() {
    if (max.size() == min.size()) {
        return (max.peek() + min.peek())/2.0;
    }
    return (double)max.peek();
}

```



8/23 [958. 回文数据流](https://www.lintcode.com/problem/palindrome-data-stream/description)

题意：每次读入一个字符，判断构成的字符串是不是回文。

不是自己的代码。O(n)做法。哎。。

```python
class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        # Write your code here
        count = collections.defaultdict(int)
        ans = []
        oddCount = 0
        for i in range(len(s)):
            count[s[i]] += 1
            if count[s[i]] % 2 == 1:
                oddCount += 1
            else:
                oddCount -= 1
            if oddCount > 1:
                ans.append(0)
            else:
                ans.append(1)
        return ans
```



8/22 [960. First Unique Number in a Stream II](https://www.lintcode.com/problem/first-unique-number-in-a-stream-ii/description)

不断读取数字，实时返回第一个独特数字。

下面的，不是自己的代码。。思路不难但要学会用collections的容器。。[here](https://docs.python.org/2/library/collections.html#)  

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