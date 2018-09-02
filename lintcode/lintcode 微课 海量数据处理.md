8.31 复习

[面试题：求两个超大文件中 URLs 的交集](https://www.jiuzhang.com/tutorial/big-data-interview-questions/269)

最佳方法：外排序。把大文件分成若干小文件，小文件内部进行快排序返回结果，之后将若干结果多路归并。归并过程自然知道哪些是重复的。

最高频k项
1 是否要精确
2 离线在线。在线的还是很难的。

容器排序：Collections.sort() 

StringTokenizer(), hasMoreTokens, nextToken

private Comparator<Pair> PairComparator = new Comparator<Pair>(){ 

​	public int compare(Pair a, Pair b){ 	}

};

**java在使用类构造函数要加new，python不用。**

8/29(8/1) [577. 合并K个排序间隔列表 ](https://www.lintcode.com/problem/merge-k-sorted-interval-lists/description)<br>

类似的思路，用一个优先队列。注意的地方，List取元素用get不是[]。任何容器取元素前注意判断是否为空。

```java
public class Solution {
    /**
     * @param intervals: the given k sorted interval lists
     * @return:  the new sorted interval list
     */
    public class Pair {
        Interval inter;
        int id;
        Pair(Interval inter, int id){
            this.inter = inter; this.id = id;
        }
    }
    private Comparator<Pair> Cmp = new Comparator<Pair>(){
        public int compare(Pair a, Pair b){
            return a.inter.start - b.inter.start;
        }
    };
    public List<Interval> mergeKSortedIntervalLists(List<List<Interval>> intervals) {
        // write your code here
        Queue<Pair> pq = new PriorityQueue<Pair>(Cmp);
        int len = intervals.size();
        int [] pointers = new int[len];
        for(int i = 0; i<len; ++i){
            if(pointers[i] < intervals.get(i).size()) 
                pq.offer(new Pair(intervals.get(i).get(pointers[i]++), i));
        }
        List<Interval> res = new ArrayList<Interval>();
        
        while(!pq.isEmpty()){
            Pair top = pq.poll();
            int i = top.id;
            if(res.size() == 0){
                res.add(top.inter);
            }
            else{
                Interval last = res.get(res.size() - 1);
                int left = last.start, right = last.end;
                if(top.inter.start <= right){
                    res.get(res.size() - 1).end = Math.max(top.inter.end, right);
                }
                else{
                    res.add(top.inter);
                }
                
            }
            if(pointers[i] < intervals.get(i).size()) 
                pq.offer(new Pair(intervals.get(i).get(pointers[i]++), i));
        }
        return res;
    }
}
```



8/21 [642. Moving Average from Data Stream](https://www.lintcode.com/problem/moving-average-from-data-stream/description)

```java
public class MovingAverage {
    Queue<Integer> qu;
    int size;
    long sum;
    public MovingAverage(int size) {
        // do intialization if necessary
        qu = new ArrayDeque<>();
        this.size = size; sum = 0;
    }

    public double next(int val) {
        // write your code here
        if(qu.size() == size){
            sum -= qu.peek();
            qu.poll();
        }
        qu.offer(val);
        sum += val;
        return sum*1.0/qu.size();
    }
}
```



7/30 [486. Merge K Sorted Arrays ](https://www.lintcode.com/problem/merge-k-sorted-arrays/description)<br>

外排序。链表和数组大同小异，关键点都在于比较器的写法，以及最小堆的操作。python牛逼。。比较函数都省了。以下代码来自LeetCode解答。

```python
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
```



```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public class Pair{
        ListNode node; int id;
        public Pair(ListNode n, int i){
            node = n; id = i;
        }
    }
    private Comparator<Pair> PairComparator = new Comparator<Pair>(){
        public int compare(Pair a, Pair b){
            return a.node.val!=b.node.val ? a.node.val - b.node.val : a.id - b.id;
        }
    };
    public ListNode mergeKLists(ListNode[] lists) { // not List<ListNode>
        int size = lists.length; //int size = lists.size();
        Queue<Pair> min_heap = new PriorityQueue<Pair>(PairComparator);
        
        ListNode [] index = new ListNode[size];
        for(int i=0; i<size; ++i){
            index[i] = lists[i];
        }
        for(int i=0; i<size; ++i){
            if(index[i]!=null){
                min_heap.offer(new Pair(index[i], i));
                index[i] = index[i].next;
            }
        }
        ListNode res = null, pre = new ListNode(0);
        while(!min_heap.isEmpty()){
            Pair top = min_heap.peek();
            int id = top.id;
            if(res == null) res = top.node;
            pre.next = top.node; pre = pre.next;
            min_heap.poll();
            if(index[id] != null) {
                min_heap.offer(new Pair(index[id], id));
                index[id] = index[id].next;
            }
        }
        return res;
    }
}
```

7/31 [550. 最常使用K个单词2](https://www.lintcode.com/problem/top-k-frequent-words-ii/description)<br>

困难题。数据流。要实现add和topK两个函数。为什么微课里面的HashHeap用不了呢。。。python要怎么实现？

```java
public class TopK {
    private Map<String, Integer> words = null;
    private NavigableSet<String> topk = null;
    private int k;
    
    private Comparator<String> myComparator = new Comparator<String>() {
        public int compare(String left, String right) {
            if (left.equals(right))
                return 0;
    
            int left_count = words.get(left);
            int right_count = words.get(right);
            if (left_count != right_count) {
                return right_count - left_count;
            }
            return left.compareTo(right);
        }
    };
    
    public TopK(int k) {
        // initialize your data structure here
        this.k = k;
        words = new HashMap<String, Integer>();
        topk = new TreeSet<String>(myComparator);
    }
    
    public void add(String word) {
        // Write your code here
        if (words.containsKey(word)) {
            if (topk.contains(word))
                topk.remove(word);
            words.put(word, words.get(word) + 1);
        } else {
            words.put(word, 1);
        }
    
        topk.add(word);
        if (topk.size() > k) {
            topk.pollLast();
        }
    }
    
    public List<String> topk() {
        // Write your code here
        List<String> results = new ArrayList<String>();
        Iterator it = topk.iterator();
        while(it.hasNext()) {
             String str = (String)it.next();
             results.add(str);
        }
        Collections.sort(results, myComparator);
        return results;
    }
}
```

其他方法参见[leetcode 离线版topKwords](https://leetcode.com/problems/top-k-frequent-words/discuss/)



7/27 [556. Standard Bloom Filter](https://www.lintcode.com/problem/standard-bloom-filter/description)<br>

代码参见两个filter代码文件，py和java。大同小异。都是k个哈希函数一起判断。


7/27 [128. Hash Function](https://www.lintcode.com/problem/hash-function/description)<br>
为后面布隆过滤准备的。python，ord(c)可以返回字符的ASCII码

7/26 [前K大数 II](https://www.lintcode.com/problem/top-k-largest-numbers-ii/description)<br>

相比1，数据量更大，所以必须使用小根堆。

自己用数组实现小根堆优先队列的代码在[这里](https://www.lintcode.com/submission/15383160/)

7/26 [544. 前K大数](https://www.lintcode.com/problem/top-k-largest-numbers/description)<br>
用优先队列实现最小堆，已经默认小的元素优先级高。容量k，插入O(K),取出前K个O(KlogK)。

```java
int max_size;
public int[] topk(int[] nums, int k) {
    Queue<Integer> min_heap = new PriorityQueue<>(k);
    max_size = k;
    for(int num: nums){
        if(min_heap.size() < max_size){
            min_heap.offer(num);
        }
        else if(num > min_heap.peek()){
            min_heap.poll();
            min_heap.offer(num);
        }
    }
    int [] res = new int[k];
    for(int i=0; i<k; ++i){
        res[k-1-i] = min_heap.poll();
    }
    return res;
}
```