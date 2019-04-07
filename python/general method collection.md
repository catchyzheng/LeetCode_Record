[Sliding Window algorithm template to solve all the Leetcode substring search problem.](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/discuss/49708/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.)

还有一题没看。



[one iterative inorder traversal, apply it to multiple tree questions (Java Solution)](https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution))

[606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/description/)

[536. Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100359/Java-stack-solution) stack solution 虽然不是高频题但还是可以看一下。。



中序遍历的迭代实现比较好理解。

```java
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> list = new ArrayList<>();
    if(root == null) return list;
    Stack<TreeNode> stack = new Stack<>();
    while(root != null || !stack.empty()){
        while(root != null){
            stack.push(root);
            root = root.left;
        }
        root = stack.pop();
        list.add(root.val);
        root = root.right;
        
    }
    return list;
}
```



前序遍历的迭代式实现。用stack。感觉有点小难理解。。。

```python
# iterative preorder traversal with stack 
sta = []
sta.append(t)
set_ = set()
res = []
while len(sta) > 0:
    t = sta[-1]
    if t in set_:
        sta.pop()
    else:
        set_.add(t)
        res.append(t.val)
        #if t.left is None and t.right is not None:
        #    res.append('()')
        if t.right is not None:
            sta.append(t.right)
        if t.left is not None:
            sta.append(t.left)
    for ele in sta:
        print(ele.val, ' ', end = '')
    print()

return res
```



[A general approach to backtracking questions in Java (Subsets, Permutations, Combination Sum, Palindrome Partitioning)](https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning))



