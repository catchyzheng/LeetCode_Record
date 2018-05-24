5.24 [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)<br>
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


