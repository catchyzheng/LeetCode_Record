5/28 [654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/description/)<br>
给定一数组，每次挑出最大元素作为根节点。然后从左边剩余部分挑最大作为左子节点，右边最大作为右子节点，循环下去。要求返回构建的树的根。<br>
递归容易，难就在于迭代式。。在lintcode上只能用迭代。因为递归溢出。<br>
```
public TreeNode maxTree(int[] nums) {
    Deque<TreeNode> stack = new LinkedList<>();
    for(int i = 0; i < nums.length; i++) {
        TreeNode curr = new TreeNode(nums[i]);
        while(!stack.isEmpty() && stack.peek().val < nums[i]) {
            curr.left = stack.pop();
        }
        if(!stack.isEmpty()) {
            stack.peek().right = curr;
        }
        stack.push(curr);
    }
    return stack.isEmpty() ? null : stack.removeLast();
}
```
```
public TreeNode constructMaximumBinaryTree(int[] nums) {
    TreeNode root = div(nums, 0, nums.length-1);
    return root;
}
TreeNode div(int [] nums, int i, int j){
    if(i>j) return null;
    if(i==j) return new TreeNode(nums[i]);
    int max_=Integer.MIN_VALUE, index=0;
    int k;
    for(k=i; k<=j; ++k){
        if(nums[k]>max_) {
            max_=nums[k]; index=k; 
        }
    }
    TreeNode node = new TreeNode(max_);
    node.left = div(nums, i, index-1);
    node.right = div(nums, index+1, j);
    return node;
}
```

5/24 [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)<br>
中序遍历一棵树。递归遍历很简单，但如何迭代地遍历呢？这才是follow up的难点。<br>
还没看。。之后有机会看看。

[108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)<br>
[109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/) together<br>
you should always notice the marginal condition. consider every special cases.
```
int [] Nums;
public TreeNode sortedArrayToBST(int[] nums) {
    int len = nums.length;
    if(len==0) return null;//very important!
    Nums = new int[len];
    Nums = nums;
    TreeNode root = new TreeNode(nums[len/2]);
    root.left = dfs(Nums, 0, len/2-1);
    root.right = dfs(Nums, len/2+1, len-1);
    return root;
}
TreeNode dfs(int [] nums, int s, int e){
    if(s>e) return null;
    if(s==e) return new TreeNode(nums[s]);
    int len = e-s+1;
    TreeNode root = new TreeNode(nums[s+len/2]);
    root.left = dfs(nums, s, s+len/2-1);
    root.right = dfs(nums, s+len/2+1, e);
    return root;
}
```


