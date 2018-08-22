8/21 [155. Min Stack](https://leetcode.com/problems/min-stack/description/)

在stack基础上加上，返回最小值的功能。

解法：我的方法是，用一个stack和一个小根堆同时存放。

vote2的解法是，多次存储min值。其实。。存放次数也差不多两次了。

```java
class MinStack {
    int min = Integer.MAX_VALUE;
    Stack<Integer> stack = new Stack<Integer>();
    public void push(int x) {
        // only push the old minimum value when the current 
        // minimum value changes after pushing the new value x
        if(x <= min){          
            stack.push(min);
            min=x;
        }
        stack.push(x);
    }
    public void pop() {
        // if pop operation could result in the changing of the current minimum value, 
        // pop twice and change the current minimum value to the last minimum value.
        if(stack.pop() == min) min=stack.pop();
    }
    public int top() {
        return stack.peek();
    }
    public int getMin() {
        return min;
    }
}
```



8/21 [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/)

用两个stack模拟。push复杂度O(n)，pop O(1)。

8/21 [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)

两个queue模拟。



