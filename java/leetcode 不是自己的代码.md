8/25 [726. Number of Atoms](https://leetcode.com/problems/number-of-atoms/description/)

题意：给出一个化学分子式，要求返回按照字母排序的所有原子元素的计数。

妙啊，写了一个parser。hard

```python
class Solution(object):
    def countOfAtoms(self, formula):
        def parse():
            N = len(formula)
            count = collections.Counter()
            while (self.i < N and formula[self.i] != ')'):
                if (formula[self.i] == '('):
                    self.i += 1
                    for name, v in parse().items():
                        count[name] += v
                else:
                    i_start = self.i
                    self.i += 1
                    while (self.i < N and formula[self.i].islower()):
                        self.i += 1
                    name = formula[i_start: self.i]
                    i_start = self.i
                    while (self.i < N and formula[self.i].isdigit()):
                        self.i += 1
                    count[name] += int(formula[i_start: self.i] or 1)
            self.i += 1
            i_start = self.i
            while (self.i < N and formula[self.i].isdigit()):
                self.i += 1
            if (i_start < self.i):
                multiplicity = int(formula[i_start: self.i])
                for name in count:
                    count[name] *= multiplicity

            return count

        self.i = 0
        ans = []
        count = parse()
        for name in sorted(count):
            ans.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)
```



8/20 [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

题意：如题目所示，要求O(log(m+n))完成。

代码如下，思路从lintcode推送获得。

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m==0 and n==0: return 0.0
        if (m+n) % 2 == 1:
            return self.kthlargest(nums1, nums2, (m+n)/2 + 1) * 1.0
        else:
            a = self.kthlargest(nums1, nums2, (m+n)/2)
            b = self.kthlargest(nums1, nums2, (m+n)/2 + 1)
            return (a+b)/2.0
    
    def kthlargest(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m==0: return nums2[k-1]
        if n==0: return nums1[k-1]
        if k == 1: return min(nums1[0], nums2[0])
        mid = k/2
        a, b = float("inf"), float("inf")
        if m >= mid: 
            a = nums1[mid-1]
        if n>= mid:
            b = nums2[mid-1]
        if a>b:
            return self.kthlargest(nums1, nums2[mid:], k - mid)
        else:
            return self.kthlargest(nums1[mid:], nums2, k - mid)
```



7/20 [72. Edit Distance](https://leetcode.com/problems/edit-distance/description)<br>

题意：给定两个字符串S,T，可以进行修改，插入，删除字符操作。问至少要多少次操作才能让S变成T。

动规题。答案解释在[这里](https://leetcode.com/problems/edit-distance/discuss/25846/20ms-Detailed-Explained-C++-Solutions-(O(n)-Space)<br>



7/14 [859. Buddy Strings](https://leetcode.com/problems/buddy-strings/description/)<br>
题意：给定两个字符串，问是否能够通过交换两个位置的字符，让它们变成相同串。<br>
思路不难。重点是学习python的语言表达.

```python
def buddyStrings(self, A, B):
    if len(A) != len(B): return False
    if A == B:
        seen = set()
        for a in A:
            if a in seen:
                return True
            seen.add(a)
        return False
    else:
        list = []
        for i in range(len(A)):
            if A[i] != B[i]: list.append(i)
        return len(list) == 2 and (A[list[0]] == B[list[1]] and A[list[1]] == B[list[0]])
        '''
        pairs = []
        for a, b in itertools.izip(A, B):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
```
7/11 [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/description/)<br>
题意：给出一个由(,)构成的串，找到最长的合法串。<br>
第一道hard题目。。纯粹看答案咯。。<br>

```
public int longestValidParentheses(String s) {
    int len = s.length();
    int [] dp = new int[len];
    int max_ = 0;
    for(int i=1; i<len; ++i){
        if(s.charAt(i)==')'){
            if(s.charAt(i-1)=='(') dp[i] = (i-2>=0 ? dp[i-2] : 0) + 2;
            else{
                if(i-1-dp[i-1] >=0 && s.charAt(i-1-dp[i-1]) == '('){
                    dp[i] = dp[i-1] + (i-1-dp[i-1]-1 >= 0 ? dp[i-2-dp[i-1]] : 0) + 2;
                }
            }
        }
        max_ = Math.max(max_, dp[i]);
    }
    return max_;
}
```

7/8 [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)<br>
题意：给定一个矩阵，找到第k大元素。矩阵从左到右，从上到下都是升序。<br>
相关题目：k-th各种。Find K Pairs with Smallest Sums
```
public int kthSmallest(int[][] matrix, int k) {
    int r = matrix.length;
    int c = (r==0 ? 0 : matrix[0].length);
    if(r==1&&c==1) return matrix[0][0];
    int low = 0, high = matrix[r-1][c-1] , mid;
    while(low < high){
        mid = low + (high-low)/2;
        int i=0, j = c-1;
        int cnt = 0;
        for(i=0; i<r; ++i){
            while(j>=0 && matrix[i][j] > mid) j--;
            cnt += j+1;
        }
        if(cnt < k) low = mid+1;
        else high = mid;
    }
    return low;
}
```
还有一个做法，用[heap](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code)

7/6 [811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/discuss/121738/C++JavaPython-Easy-Understood-Solution)<br>
题意：给定一系列域名和对应的访问次数，求所有域名子域名的访问次数。例如["900 discuss.baidu.com", "50 fake.com"],那么应该返回 ["900 discuss.baidu.com", "900 baidu.com", "50 fake.com", "950 com"].<br>
py强大啊。。。
```
def subdomainVisits(self, cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in xrange(len(frags)):
            ans[".".join(frags[i:])] += count

    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
    # return ["{} {}".format(ans[c], c) for c in ans]
```

[343. Integer Break](https://leetcode.com/problems/integer-break/description/)<br>
dp, or math approach.

[221. Maximal Square](https://leetcode.com/problems/maximal-square/solution/)<br>
在一个01矩阵中找到最大的全1的正方形。<br>

```
public int maximalSquare(char[][] matrix) {
    int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
    int[][] dp = new int[rows + 1][cols + 1];
    int maxsqlen = 0;
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            if (matrix[i-1][j-1] == '1'){
                dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
                maxsqlen = Math.max(maxsqlen, dp[i][j]);
            }
        }
    }
    return maxsqlen * maxsqlen;
}
```

[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)<br>
找到最长的上升子序列。不一定要连续。
动规。其实思路不难的。。。
```
public int lengthOfLIS(int[] nums) {
    if (nums.length == 0) {
        return 0;
    }
    int[] dp = new int[nums.length];
    dp[0] = 1;
    int maxans = 1;
    for (int i = 1; i < dp.length; i++) {
        int maxval = 0;
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                maxval = Math.max(maxval, dp[j]);
            }
        }
        dp[i] = maxval + 1;
        maxans = Math.max(maxans, dp[i]);
    }
    return maxans;
}
```

[264. Ugly Number II](https://leetcode.com/problems/ugly-number-ii/description/)<br>
丑数定义为只能被2，3，5整除的数。要求在O(n)内找到第n个丑数。<br>
新建一个数组k表示丑数序列，第一个为k[0] = 1.然后
k[1] = min( k[0]x2, k[0]x3, k[0]x5). 答案是k[0]x2. 于是移动2的下标，增加1. 之后尝试:
k[2] = min( k[1]x2, k[0]x3, k[0]x5). 等等. 注意，对于6这类数，应该对2和3的下标都增加 1.
[code is here](https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C++-DP-solution-with-short-explanation)<br>

[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)<br>
寻找乘积最大的子序列。
下面是投票最多的解法。很巧妙。
```
int maxProduct(int A[], int n) {
    // store the result that is the max we have found so far
    int r = A[0];
    // imax/imin stores the max/min product of
    // subarray that ends with the current number A[i]
    for (int i = 1, imax = r, imin = r; i < n; i++) {
        // multiplied by a negative makes big number smaller, small number bigger
        // so we redefine the extremums by swapping them
        if (A[i] < 0)
            swap(imax, imin);
        // max/min product for the current number is either the current number itself
        // or the max/min by the previous number times the current one
        imax = max(A[i], imax * A[i]);
        imin = min(A[i], imin * A[i]);
        // the newly computed max value is a candidate for our global result
        r = max(r, imax);
    }
    return r;
}
```

[646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/description/)<br>
有dp的做法，也有greedy的做法。[here](https://leetcode.com/problems/maximum-length-of-pair-chain/solution/)
别人的贪心做法：
这个Arrays.sort写得好！还有这个foreach循环真棒。
```
public int findLongestChain(int[][] pairs) {
    Arrays.sort(pairs, (a, b) -> a[1] - b[1]);
    int cur = Integer.MIN_VALUE, ans = 0;
    for (int[] pair: pairs) {
		if (cur < pair[0]) {
	        cur = pair[1];
	        ans++;
	    }
	}	
    return ans;
}
```
自己的贪心做法。
```
public int findLongestChain(int[][] p) {
    if(p.length<=1) return p.length;
    for(int i=0; i<p.length-1; i++){
        for(int j=i+1; j<p.length; j++){
            if(p[j][1]<p[i][1]){
                int tmp1=p[i][0], tmp2=p[i][1];
                p[i][0]=p[j][0]; p[i][1]=p[j][1];
                p[j][0]=tmp1; p[j][1]=tmp2;
            }
        }
    }
    int cnt=1;
    int end=p[0][1];
    for(int s=1; s<p.length; s++){
        if(p[s][0]>end){
            cnt++;
            end=p[s][1];
        }
    }
    return cnt;
}
```

[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/solution/)<br>
判断一棵树是否是轴对称。<br>
recursive
```
public boolean isSymmetric(TreeNode root) {
    return isMirror(root, root);
}
public boolean isMirror(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    return (t1.val == t2.val)
        && isMirror(t1.right, t2.left)
        && isMirror(t1.left, t2.right);
}
```
iterative
```
public boolean isSymmetric(TreeNode root) {
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    q.add(root);
    while (!q.isEmpty()) {
        TreeNode t1 = q.poll();
        TreeNode t2 = q.poll();
        if (t1 == null && t2 == null) continue;
        if (t1 == null || t2 == null) return false;
        if (t1.val != t2.val) return false;
        q.add(t1.left);
        q.add(t2.right);
        q.add(t1.right);
        q.add(t2.left);
    }
    return true;
}
```

[112. Path Sum](https://leetcode.com/problems/path-sum/discuss/36378/AcceptedMy-recursive-solution-in-Java)<br>
判断能否从根节点到某个叶子节点的路径和等于指定值。<br>
下面是最简洁的做法。直接依次减，减到0就行。
```
public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null) return false;
        //
        if(root.left == null && root.right == null && sum - root.val == 0) return true;
    	//
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
```
自己的做法，记录路径上各个元素，递归。这才是实现了我想要的！哼
```
class Solution {
public:
    vector<int> vec;
    bool isequal=false;
    bool hasPathSum(TreeNode* root, int sum) {
        dfs(root, sum); return isequal;
    }
    void dfs(TreeNode * root, int sum){
        if(root==NULL) return;
        vec.push_back(root->val);
        if(root->left==NULL&&root->right==NULL){
            int tmp=0;
            for(int i=0;i<vec.size();i++) tmp+=vec[i];
            if(tmp==sum) isequal=true;
            vec.pop_back(); return;
        }
        if(!isequal) { dfs(root->left, sum); dfs(root->right, sum); }
        vec.pop_back(); return;
    }
};
```

[695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/discuss/108533/JavaC++-Straightforward-dfs-solution)<br>
题意：找出一个01矩阵中最大的一片1的面积。
典型dfs。

```
public int maxAreaOfIsland(int[][] grid) {
    int max_area = 0;
    for(int i = 0; i < grid.length; i++)
        for(int j = 0; j < grid[0].length; j++)
            if(grid[i][j] == 1) max_area = Math.max(max_area, AreaOfIsland(grid, i, j));
    return max_area;
}
public int AreaOfIsland(int[][] grid, int i, int j){
    if( i >= 0 && i < grid.length && j >= 0 && j < grid[0].length && grid[i][j] == 1){
        grid[i][j] = -1; // visited is -1
        return 1 + AreaOfIsland(grid, i+1, j) + AreaOfIsland(grid, i-1, j) + AreaOfIsland(grid, i, j-1) + AreaOfIsland(grid, i, j+1);
    }
    return 0;
}
```

[168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/)<br>
excel中列的数字字母转换。大神的代码。。简洁得无可挑剔。<br>
1 -> A, 2 -> B, 3 -> C... 26 -> Z, 27 -> AA, 28 -> AB 
```
return n == 0 ? "" : convertToTitle((n - 1) / 26) + (char) ((n - 1) % 26 + 'A');
```
[500. Keyboard Row](https://leetcode.com/problems/keyboard-row/description/)<br>
判断一个单词是否能够只用键盘上的一行字母构成。<br>

```
public class Solution {
    public String[] findWords(String[] words) {
        String[] strs = {"QWERTYUIOP","ASDFGHJKL","ZXCVBNM"};
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i<strs.length; i++){
            for(char c: strs[i].toCharArray()){
                map.put(c, i);//put <char, rowIndex> pair into the map
            }
        }
        List<String> res = new LinkedList<>();
        for(String w: words){
            if(w.equals("")) continue;
            int index = map.get(w.toUpperCase().charAt(0));
            for(char c: w.toUpperCase().toCharArray()){
                if(map.get(c)!=index){
                    index = -1; //don't need a boolean flag. 
                    break;
                }
            }
            if(index!=-1) res.add(w);//if index != -1, this is a valid string
        }
        return res.toArray(new String[0]);
    }
}
```

[617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/discuss/104299/Java-Solution-6-lines-Tree-Traversal)<br>
题意：从根部合并两个树。要牢记实现的细节！PS:这不是自己的代码

```
public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return null;
    
    int val = (t1 == null ? 0 : t1.val) + (t2 == null ? 0 : t2.val);
    TreeNode newNode = new TreeNode(val);
    
    newNode.left = mergeTrees(t1 == null ? null : t1.left, t2 == null ? null : t2.left);
    newNode.right = mergeTrees(t1 == null ? null : t1.right, t2 == null ? null : t2.right);
    
    return newNode;
}
```
[669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/description/)<br>
题意：给定一个BST,要求去除值在[L,R]外的节点(R >= L).有可能会改变树根。PS:这不是自己的代码
```
class Solution {
    public TreeNode trimBST(TreeNode root, int L, int R) {
        if (root == null) return null;
        if (root.val < L) return trimBST(root.right, L, R);
        if (root.val > R) return trimBST(root.left, L, R);
        //
        root.left = trimBST(root.left, L, R);
        root.right = trimBST(root.right, L, R);
        return root;
    }
}
```
[448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)<br>
一个长为n的数组，元素都是1<=a[i]<=n。有些数出现了两次有些出现了一次。找到那些没出现的数。
我只能说，如果不准新开数组，这题真的挺不easy的。。如果把所有值减一，然后把a[i]=j视为从i到j的有向边，那么要找的就是没有入边的节点。<br>
```
public List<Integer> findDisappearedNumbers(int[] nums) {
    List<Integer> ret = new ArrayList<Integer>();
    
    for(int i = 0; i < nums.length; i++) {
        int val = Math.abs(nums[i]) - 1;
        if(nums[val] > 0) {
            nums[val] = -nums[val];
        }
    }
    
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] > 0) {
            ret.add(i+1);
        }
    }
    return ret;
}
```
[442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/)<br>
题意：一个长为n的数组由1-n中的数字组成。找出所有出现两次的数字。<br>
解法：从448的思路稍微改改就行。看看日后你能想到否？<br>

[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)<br>
题意：把一个数组中的所有0都移到末尾，同时保持其他元素的相对顺序。不能copy数组，只能在原数组上操作。<br>
这个思路好棒啊，O(n)就行了。<br>
双下标法，一个慢一个快。其中的精髓是要逆向思考，也就是说并不是对题目特定数操作，而是在非特定数才操作。比如这题就不是对0元素操作而是非0元素。<br>
```
public void moveZeroes(int[] nums) {
    int j = 0;
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] != 0) {
            int temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;
            j++;
        }
    }
}
```

[27. Remove Element](https://leetcode.com/problems/remove-element/description/)<br>
题意，在原数组上移除所有指定值元素。<br>
又一个双下标法。<br>
```
public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
```
[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)<br>
双下标试试看。<br>

[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)<br>
找到子序列的最大和。 <br>
解法：实际上是挺简单的DP，但你还是不会！看代码吧。
```
    private int[] sum;
    public int maxSubArray(int[] nums) {
        if(nums.length==0) return 0;
        int [] dp = new int[nums.length+1];
        dp[0]=0;
        int max_=nums[0];
        for(int i=1;i<=nums.length;i++){
            dp[i]=nums[i-1]+(dp[i-1]>0 ? dp[i-1] : 0);
            max_=Math.max(dp[i], max_);
        }
        return max_;
    }
```

[697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/)<br>
题意：一个数组的度定义为出现次数最多的元素的出现次数。求最短子序列的长度，且子序列有相同度。<br>
扫描，记录每个元素第一次出现和最后一次出现的下标，记为left和right，然后取度数最大且最短的就行。<br>
以下是**别人家的代码**。。思路不难，主要是熟悉java语法。<br>
```
class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> left = new HashMap(),
            right = new HashMap(), count = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (left.get(x) == null) left.put(x, i);
            right.put(x, i);
            count.put(x, count.getOrDefault(x, 0) + 1);
        }
        int ans = nums.length;
        int degree = Collections.max(count.values());
        for (int x: count.keySet()) {
            if (count.get(x) == degree) {
                ans = Math.min(ans, right.get(x) - left.get(x) + 1);
            }
        }
        return ans;
    }
}
```
[796. Rotate String](https://leetcode.com/problems/rotate-string/description/)<br>
题意：判断一个字符串能不能通过字母平移得到另一个串。<br>
简单的return (A+A).contains(B)，但复杂度是N2。其实有N的，要用到大数哈希了。[solution](https://leetcode.com/problems/rotate-string/solution/)

[]()
```

```