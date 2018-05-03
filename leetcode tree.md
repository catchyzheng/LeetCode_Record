[814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/description/)<br>
题意：自下往上，砍掉所有值为0的叶子节点。<br>
**重点**：不要光顾着砍掉目前的0值叶子。
```
public TreeNode pruneTree(TreeNode root) {
    if(root==null) return null;
    return dfs(root);
}
public TreeNode dfs(TreeNode root){
    if(root.val==0 && root.left==null && root.right==null) return null;
    if(root.left!=null) root.left = dfs(root.left);
    if(root.right!=null) root.right = dfs(root.right);
    if(root.val==0 && root.left==null && root.right==null) return null;
    else return root;
}
```

[637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/)<br>
题意：找到树每层节点的平均值。<br>
dfs或者bfs。这里的bfs可以有不记录层数的方法，即队列里只需要放入节点元素。参见以下solution代码。
```
public List < Double > averageOfLevels(TreeNode root) {
    List < Double > res = new ArrayList < > ();
    Queue < TreeNode > queue = new LinkedList < > ();
    queue.add(root);
    while (!queue.isEmpty()) {
        long sum = 0, count = 0;
        Queue < TreeNode > temp = new LinkedList < > ();
        while (!queue.isEmpty()) {
            TreeNode n = queue.remove();
            sum += n.val;
            count++;
            if (n.left != null)
                temp.add(n.left);
            if (n.right != null)
                temp.add(n.right);
        }
        queue = temp;
        res.add(sum * 1.0 / count);
    }
    return res;
}
```
如何知道队列中的元素是不是来自同一层呢？方法是用两个队列，将该层节点的子节点存入另一个队列中。之后在copy过来，继续。

[107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34981/My-DFS-and-BFS-java-solution)<br>
给一个二叉树，返回自底向上的水平遍历。<br>
BFS:和102的基本一致，只需将改成add(0, subList)在0下标处插入subList。
DFS:看看，学习。
```
public List<List<Integer>> levelOrderBottom(TreeNode root) {
    List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
    levelMaker(wrapList, root, 0);
    return wrapList;
}
public void levelMaker(List<List<Integer>> list, TreeNode root, int level) {
    if(root == null) return;
    if(level >= list.size()) {
        list.add(0, new LinkedList<Integer>());
    }
    levelMaker(list, root.left, level+1);
    levelMaker(list, root.right, level+1);
    list.get(list.size()-level-1).add(root.val);
}
```
[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)<br>
给一个二叉树，返回从上到下的水平遍历。<br>
我自己也做出来啦！！然而是C++的BFS想了好久。。哭<br>
好好学学人家的BFS怎么用java写。。。其实答案还没看懂。。<br>
```
public List<List<Integer>> levelOrder(TreeNode root) {
    Queue<TreeNode> queue = new LinkedList<TreeNode>();
    List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
    //
    if(root == null) return wrapList;
    //
    queue.offer(root);
    while(!queue.isEmpty()){
        int levelNum = queue.size();
        List<Integer> subList = new LinkedList<Integer>();
        for(int i=0; i<levelNum; i++) {
            if(queue.peek().left != null) queue.offer(queue.peek().left);
            if(queue.peek().right != null) queue.offer(queue.peek().right);
            subList.add(queue.poll().val);
        }
        wrapList.add(subList);
    }
    return wrapList;
}
```
[103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)<br>
5.3更新：下次做一下。<br>4.21更新：**还没做别瞎比比。**呃，其实不就是102的做法后将二维vector数组每层反转一下就行吗。。

[508. Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/description/)<br>
找出最频繁的子树和。子树和定义为一棵子树上所有节点的和。
```
class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    int max_=0;
    public int[] findFrequentTreeSum(TreeNode root) {
        dfs(root);
        List<Integer> res = new ArrayList<>();
        for(int key : map.keySet()){
            if(map.get(key)==max_) {res.add(key);}
        }
        int [] ans = new int[res.size()];
        for(int i=0;i<res.size();i++) ans[i]=res.get(i);
        return ans;
    }
    int dfs(TreeNode p){
        if(p==null) return 0;
        else {
            int sum = p.val+dfs(p.left)+dfs(p.right);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
            max_ = Math.max(max_, map.get(sum));
            return sum;
        }
    }
}
```
[572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/)<br>
判断t是否是s的子树。注意子树可以是树本身。
答案的做法，第一种是用后序遍历生成一个字符串，然后判断第二个字符串是否被第一个包含。<br>
第二种方法和我一样，甚至速度还没我的快。。
```
public class Solution {
    HashSet < String > trees = new HashSet < > ();
    public boolean isSubtree(TreeNode s, TreeNode t) {
        String tree1 = preorder(s, true);
        String tree2 = preorder(t, true);
        return tree1.indexOf(tree2) >= 0;
    }
    public String preorder(TreeNode t, boolean left) {
        if (t == null) {
            if (left) return "lnull";
            else return "rnull";
        }
        return "#"+t.val + " " +preorder(t.left, true)+" " +preorder(t.right, false);
    }
}
```
第二种方法，自己的代码，很开心，美滋滋。
```
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(t==null) return true;
        if(s==null) return false;
        return dfs(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t); 
    }
    boolean dfs(TreeNode s, TreeNode t){
        if(s==null && t==null) return true;
        else if(s==null || t==null) return false;
        else return s.val==t.val && dfs(s.left, t.left) && dfs(s.right, t.right);
    }
}
```

[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)<br>
找出树的直径：两个叶子的最大距离为直径。
```
class Solution {
    int longest=0;
    public int diameterOfBinaryTree(TreeNode root) {
        int depth = dfs(root);
        return longest;
    }
    public int dfs(TreeNode root){
        if(root==null) return 0;
        int left = dfs(root.left);
        int right = dfs(root.right);
        longest = Math.max(longest, left+right);
        return 1+Math.max(left, right);
    }
}
```

[563. Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/description/)<br>
题意：Given a binary tree, return the tilt of the whole tree.<br>
The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.<br>
The tilt of the whole tree is defined as the sum of all nodes' tilt.<br>
```
class Solution {
    public int ans=0;
    public int findTilt(TreeNode root){
        dfs(root); return ans;
    }
    public int dfs(TreeNode root){
        if(root==null) return 0;
        int left = dfs(root.left);
        int right = dfs(root.right);
        ans+=Math.abs(left - right);
        return root.val + left + right;
    }
}
```

[404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/)<br>
把所有左叶子节点的值求和。

[112. Path Sum](https://leetcode.com/problems/path-sum/description/)<br>
题意：找到所有从根到叶子的路径，使得路径和等于指定值。路径集合用列表的列表存储。
解法：1是可以每次递归时候传入sum-node->val的值。在叶子节点处判断sum是否等于node->val。<br>
```
if(root==NULL) return;
pat.push_back(root->val); 
if(root->left==NULL && root->right==NULL){
    if(root->val==sum) ans.push_back(pat);
}
dfs(root->left, sum-root->val); dfs(root->right, sum-root->val);
pat.pop_back(); return ;
```
第二种做法是可以用变量cal记录路径和。注意路径要用一个path存储。每次递归结束返回要pop，同时cal要减掉相应值。
```
if(root==NULL) return;
pat.push_back(root->val); cal+=root->val;
if(root->left==NULL && root->right==NULL && cal==sum){
    ans.push_back(pat);
}
dfs(root->left, sum); dfs(root->right, sum);
pat.pop_back(); cal-=root->val; 
//this is backtracking. 'cal' should backtrack too. 
return ;
```

[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)<br>
对每个树节点，交换左右分支。。。
```
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return null;
        TreeNode new_root = new TreeNode(root.val);
        new_root.left = invertTree(root.right);
        new_root.right = invertTree(root.left);
        return new_root;
    }
}
```
[538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/description/)<br>
题意：给定一棵树，对所有元素，都加上比它大的元素。求最后树的模样。<br>
思路：很简单，就是先序遍历一遍，排个序累加，然后重新遍历即可。用map帮助实现。坑爹之处在于一定要**判空**，即可能是个空树。<br>


```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    map<int, int> Map;
    vector<int> oldv, newv;
    void preorder(TreeNode * root){
        if(root == NULL) return;
        else{
            oldv.push_back(root->val);
            preorder(root->left); preorder(root->right);
            return;
        }
    }
    void construct(){
        sort(oldv.begin(), oldv.end());
        int sum=0;
        for(int i=0;i<oldv.size();i++) sum+=oldv[i];
        newv.push_back(sum);
        for(int i=0;i<oldv.size()-1;i++){
            sum-=oldv[i];
            newv.push_back(sum);
        }
        for(int i=0;i<oldv.size();i++){
            Map[oldv[i]]=newv[i];
        }
    }
    TreeNode* rebuildTree(TreeNode* root){
        if(root==NULL) return NULL;
        else{
            int value = root->val;
            TreeNode *p = new TreeNode(Map[value]);
            p->left = rebuildTree(root->left);
            p->right = rebuildTree(root->right);
            return p;
        }
    }
    TreeNode* convertBST(TreeNode* root) {
        if(root==NULL) return NULL; // 奶奶的关键就在这里！要先判断，不然会出现
                                //reference binding to null pointer of type 'value_type'
        preorder(root); construct();
        return rebuildTree(root);
    }
};
```
[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)<br>
```
class Solution {
    public int maxDepth(TreeNode root) {
        if(root==null) return 0;
        else return 1 + Math.max(maxDepth(root.left), maxDepth(root.right) );
    }
}
```
[111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)<br>
大神的思路：还没搞懂。。。<br>
```
public class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        int left = minDepth(root.left);
        int right = minDepth(root.right);
        return (left == 0 || right == 0) ? left + right + 1: Math.min(left,right) + 1;
       
    }
}
```
自己的思路：BFS,记录深度。不知道java怎么写只能用c++了。。注意一定要**pop！！**<br>
```
class Solution {
public:
    queue<pair<TreeNode*, int> > Q;
    int minDepth(TreeNode* root) {
        if(root==NULL) return 0;
        else{
            int min_depth=10000;
            Q.push(make_pair(root, 1));
            while(!Q.empty()){
                TreeNode* top = Q.front().first;
                int depth = Q.front().second;
                if(top->left!=NULL) Q.push(make_pair(top->left, depth+1) );
                if(top->right!=NULL) Q.push(make_pair(top->right, depth+1) );
                Q.pop();
                if(top->left==NULL&&top->right==NULL) {
                    min_depth=depth; break;
                }
            }
            return min_depth;
        }
    }
};
```
[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)<br>
判断是否是平衡树。
```
class Solution {
    public boolean Balance = true;
    public boolean isBalanced(TreeNode root) {
        dfs(root); return Balance;
    }
    public int dfs(TreeNode root){
        if(root==null||Balance==false) return  0;
        else{
            int ltree = dfs(root.left);
            int rtree = dfs(root.right);
            if(Math.abs(ltree-rtree)>1) Balance=false;
            return 1+Math.max(ltree, rtree);
        }
    }
}
```