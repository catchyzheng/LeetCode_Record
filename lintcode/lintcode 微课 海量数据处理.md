最高频k项
1 是否要精确
2 离线在线。

7/26 [544. 前K大数](https://www.lintcode.com/problem/top-k-largest-numbers/description)<br>
用优先队列实现最小堆，已经默认小的元素优先级高。容量k，插入O(K),取出前K个O(KlogK)。
```
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