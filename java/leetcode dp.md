9/8复习起点

7/9复习起点<br>
[91. Decode Ways](https://leetcode.com/problems/decode-ways/description/)<br>
令A-Z对应1-26，现在给出一个数字构成的字符串，问有多少种解析成字母串的方法？

自己的代码。一个月后重做的。。
```
public int numDecodings(String s) {
    int len = s.length();
    if(len==0) return 0;
    if(len==1) return s.charAt(0)=='0' ? 0 : 1;
    int [] dp = new int[len+1];
    dp[0] = 1;
    dp[1] = s.charAt(0)=='0' ? 0 : 1;
    for(int i=2; i<=len; ++i){
        if(s.charAt(i-1)!='0') dp[i] += dp[i-1];
        if(s.charAt(i-2)=='1' || (s.charAt(i-2)=='2' && (s.charAt(i-1)>='0' && s.charAt(i-1)<='6') ) ) dp[i] += dp[i-2];
    }
    return dp[len];
}
```
下面不是自己的代码。但很简洁，值得学习。要考虑两个问题，1如何设计子问题，2如何根据子问题的最优解构造原问题最优解。。
```
public int numDecodings(String s) {
    int n = s.length();
    if (n == 0) return 0;
    int[] memo = new int[n+1];
    memo[n]  = 1;
    memo[n-1] = s.charAt(n-1) != '0' ? 1 : 0;
    for (int i = n - 2; i >= 0; i--)
        if (s.charAt(i) == '0') continue;
        else memo[i] = (Integer.parseInt(s.substring(i,i+2))<=26) ? memo[i+1]+memo[i+2] : memo[i+1];
    return memo[0];
}
```

[120. Triangle](https://leetcode.com/problems/triangle/description/)<br>recoded
给定一个第n行有n个元素的三角形。问从顶端走到底部的最小路径和。<br>
答案的解答。
如何迭代。也就是如何构造子问题。很关键。
```
public int minimumTotal(List<List<Integer>> triangle) {
    int[] dp = new int[triangle.size() + 1];
	//
    for (int i = triangle.size() - 1; i >= 0; i--) {
        List<Integer> list = triangle.get(i);
        for (int j = 0; j < list.size(); j++) {
            dp[j] = list.get(j) + Math.min(dp[j], dp[j + 1]);
        }
    }
    return dp[0];
}
```
自己的代码,符合自己的思路，清晰明了，也能做出。
```
public int minimumTotal(List<List<Integer>> triangle) {
    int r = triangle.size(), c;
    if(r==0) return 0;
    else c = triangle.get(r-1).size();
    if(r==1) return triangle.get(0).get(0);
    int [][] dp = new int[r][c];
    dp[0][0]=triangle.get(0).get(0);
    int min_ = Integer.MAX_VALUE;
    for(int i=1; i<r; i++){
        for(int j=0; j<=i; j++){
            if(j==0) 
				dp[i][j]=triangle.get(i).get(j) + dp[i-1][j];
            else if(j==i) 
				dp[i][j]=triangle.get(i).get(j) + dp[i-1][j-1];
            else 
				dp[i][j]=triangle.get(i).get(j) + Math.min(dp[i-1][j-1], dp[i-1][j]);
            if(i==r-1) min_ = min_ < dp[i][j] ? min_ : dp[i][j];
            System.out.print(dp[i][j]+" ");
        }
        System.out.println();
    }
    return min_;
}
```
[494. Target Sum](https://leetcode.com/problems/target-sum/solution/)<br>
给定一个数组，要在每个数前放个符号，然后求和。问有多少种方法可以让和等于指定值。<br>
DP时候，从2D降到1D基本上都是有序迭代的维度，而且下标从小到大迭代。
```
public int findTargetSumWays(int[] nums, int S) {
    int[][] dp = new int[nums.length][2001];
    dp[0][nums[0] + 1000] = 1;
    dp[0][-nums[0] + 1000] += 1;
    for (int i = 1; i < nums.length; i++) {
        for (int sum = -1000; sum <= 1000; sum++) {
            if (dp[i - 1][sum + 1000] > 0) {
                dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000];
                dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000];
            }
        }
    }
    return S > 1000 ? 0 : dp[nums.length - 1][S + 1000];
}
```
```dp[i][j]```表示，用i+1个数经过处理后，值等于j的方法数。<br>

discussion还有转化为寻找子集和的思路。然而。。
```
public int findTargetSumWays(int[] nums, int s) {
    int sum = 0;
    for (int n : nums)
        sum += n;
    return sum < s || (s + sum) % 2 > 0 ? 0 : subsetSum(nums, (s + sum) >>> 1); 
}
public int subsetSum(int[] nums, int s) {
    int[] dp = new int[s + 1]; 
    dp[0] = 1;
    for (int n : nums)
        for (int i = s; i >= n; i--)
            dp[i] += dp[i - n]; 
    return dp[s];
} 
```
？？并没有看懂。。
7/9 复习标记。

重要 [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/)<br>
如何遍历，从后往前还是从前往后也是一门学问。在没有函数辅助dp情况下，要保证每个状态转移方程等式右边的每个状态都是已经计算过的。

[96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/description/)<br>
给出n值，欲存储1-n，有多少种BST的结构。<br>
动规。
```
int len; int [] dp;
public int numTrees(int n) {
    if(n<=2) return n;
    dp = new int[n+1];
    dp[0] = dp[1]=1; dp[2]=2;
    int ans=0;
    return dfs(n);
}
int dfs(int n){
    if(dp[n]>0) return dp[n];
    int sum=0;
    for(int i=1;i<=n;i++){
        dp[i-1]=dfs(i-1);//dist:(i-1)-0
        dp[n-i]=dfs(n-i);//dist:(n+1)-(i+1)
        sum+=dp[i-1]*dp[n-i];
    }
    return sum;
}
```

[740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/description/)<br>
给定一数组，每当删除一个元素num，可以加num分，但同时也会删除所有num-1和num+1。求最多能得到多少分。<br>
典型动规。先统计出每种值的个数，找出最大最小值。然后dp。和那个house robber很像。
```
public int deleteAndEarn(int[] nums) {
    int [] cnt = new int[10000+1];
    int len = nums.length;
    int min_=1, max_=10000;
    for(int i=0;i<len;i++){
        cnt[nums[i]]++;
        min_ = min_<nums[i] ? min_ : nums[i];
        max_ = max_>nums[i] ? max_ : nums[i];
    }
    int [] dp = new int[10001];
    dp[min_]=cnt[min_]*min_; dp[min_-1]=0;
    for(int i=min_+1; i<=max_;i++){
        dp[i] = cnt[i]*i+dp[i-2] > dp[i-1] ? cnt[i]*i+dp[i-2] : dp[i-1];
    }
    return dp[max_];
}
```

[486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/description/)<br>
两人依次从一个数组两端取数字，一次取一个，A先取，最后总和最大者胜利。问理想状况下A会不会赢。<br>
自己有动规，但是效率比较低。。看看别人的[here](https://leetcode.com/problems/predict-the-winner/solution/)<br>最后的目标是**判断ScoreA-ScoreB是否>=0，即if dp[0][len-1]>=0。**<br>
确实，遍历的顺序有讲究。对于```dp[i][j]=max(nums[i]−dp[i+1][j],nums[j]−dp[i][j−1])```，i就要从大到小，j就要从小到大。
```
public boolean PredictTheWinner(int[] nums) {
    int[][] dp = new int[nums.length + 1][nums.length];
    for (int s = nums.length; s >= 0; s--) {
        for (int e = s + 1; e < nums.length; e++) {
            int a = nums[s] - dp[s + 1][e];
            int b = nums[e] - dp[s][e - 1];
            dp[s][e] = Math.max(a, b);
        }
    }
    return dp[0][nums.length - 1] >= 0;
}
```
[62. Unique Paths](https://leetcode.com/problems/unique-paths/description/)<br>
入门级别动规。给定一个二维数组长宽，求从左上角走到右下角的路径种类个数。<br>
最直观的二维DP想法很简单，但是为何能够优化到一维空间复杂度呢？值得琢磨。
```
int uniquePaths(int m, int n) {
    vector<vector<int> > path(m, vector<int> (n, 1));
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            path[i][j] = path[i - 1][j] + path[i][j - 1];
    return path[m - 1][n - 1];
}
```
```
int uniquePaths(int m, int n) {
    if (m > n) return uniquePaths(n, m);
    vector<int> cur(m, 1);
    for (int j = 1; j < n; j++)
        for (int i = 1; i < m; i++)
            cur[i] += cur[i - 1]; 
    return cur[m - 1];
}
```
[357. Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/description/)<br>
感觉和动规没什么关系。。就是一数学题。<br>
```
public static int countNumbersWithUniqueDigits(int n) {
    if (n == 0) return 1;
    int ans = 10, base = 9;
    for (int i = 2; i <= n && i <= 10; i++) {
        base = base * (9 - i + 2);
        ans += base;
    }
    return ans;
}
```
[392. isSubsequence](https://leetcode.com/problems/is-subsequence/description/)<br>
常规的双指针做法确实比较慢。<br>
follow up: 关于如果有大量数据需要比较的，该怎么做？讨论在[这里](https://leetcode.com/problems/is-subsequence/discuss/?orderBy=most_votes)<br>
[java version](https://leetcode.com/problems/is-subsequence/discuss/87302/Binary-search-solution-for-follow-up-with-detailed-comments)：
```
// Follow-up: O(N) time for pre-processing, O(Mlog?) for each S.
// Eg-1. s="abc", t="bahbgdca"
// idx=[a={1,7}, b={0,3}, c={6}]
//  i=0 ('a'): prev=1
//  i=1 ('b'): prev=3
//  i=2 ('c'): prev=6 (return true)
// Eg-2. s="abc", t="bahgdcb"
// idx=[a={1}, b={0,6}, c={5}]
//  i=0 ('a'): prev=1
//  i=1 ('b'): prev=6
//  i=2 ('c'): prev=? (return false)
public boolean isSubsequence(String s, String t) {
    List<Integer>[] idx = new List[256]; // Just for clarity
    for (int i = 0; i < t.length(); i++) {
        if (idx[t.charAt(i)] == null)
            idx[t.charAt(i)] = new ArrayList<>();
        idx[t.charAt(i)].add(i);
    }
    int prev = 0;
    for (int i = 0; i < s.length(); i++) {
        if (idx[s.charAt(i)] == null) return false; // Note: char of S does NOT exist in T causing NPE
        int j = Collections.binarySearch(idx[s.charAt(i)], prev);
        if (j < 0) j = -j - 1;
        if (j == idx[s.charAt(i)].size()) return false;
        prev = idx[s.charAt(i)].get(j) + 1;
    }
    return true;
}
```
[python version](https://leetcode.com/problems/is-subsequence/discuss/87264/Easy-to-understand-binary-search-solution):
```
from collections import defaultdict
from bisect import bisect_left
class Solution(object):
    def createMap(self, s):
        # create a map. key is char. value is index of apperance in acending order. 
        posMap = defaultdict(list)
        for i, char in enumerate(s):
            posMap[char].append(i)
        return posMap
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        posMap = self.createMap(t)
        # lowBound is the minimum index the current char has to be at.
        lowBound = 0
        for char in s:
            if char not in posMap: return False
            charIndexList = posMap[char]
            # try to find an index that is larger than or equal to lowBound
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList): return False
            lowBound = charIndexList[i] + 1
        return True
```
总结：遍历T串找到每个字母对应的所有下标，用arraylist存，已经升序。之后定一个下界prev=0，对S从头遍历，每当找到在T中的下标后就设置prev为<下标+1>。

[647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/solution/)<br>
要知道n方的动规和枚举中心点怎么做？

[338. Counting Bits](https://leetcode.com/problems/counting-bits/description/)<br>
找到指定数的二进制表示中1的个数。
a[n] = a[n/2] + n%2 <br>
[413. Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/description/)<br>
若连续三个以上的数差相同，则为算数的。问指定序列有多少个算数的子序列。
标答的dp。
```
int[] dp = new int[A.length];
int sum = 0;
for (int i = 2; i < dp.length; i++) {
    if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
        dp[i] = 1 + dp[i - 1];
        sum += dp[i];
    }
}
return sum;
//或者，维护一个变量代替dp[]数组
int dp = 0;
int sum = 0;
for (int i = 2; i < A.length; i++) {
    if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
        dp = 1 + dp;
        sum += dp;
    } else
        dp = 0;
}
return sum;
```

[304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/description/)<br>
题意：求二维矩阵中任意子矩阵和。inclusive。<br>
还是动规。trick和303一样，但**一定一定要考虑到空矩阵！！**<br>
```
class NumMatrix {
    private int[][] sum;
    public NumMatrix(int[][] mat) {
        int row = mat.length+1, col;
        if(row>1) col = mat[0].length+1;
        else col=1;
        sum = new int[row][col];
        for(int i=0;i<row-1;i++){
            for(int j=0;j<col-1;j++){
                sum[i+1][j+1] = mat[i][j]+sum[i+1][j]+sum[i][j+1]-sum[i][j];
            }
        }
    }
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sum[row2+1][col2+1]-sum[row2+1][col1]-sum[row1][col2+1]+sum[row1][col1];
    }
}
```
[303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/description/)<br>
题意：求任意子序列和。inclusive<br>
是很容易的题目，但实现上有个trick，就是因为前后包含，所以直接sum[j]-sum[i-1]会下标溢出。。所以不如直接用sum[j+1]来记录下标<=j的所有元素和。<br>
[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)<br>
题意：给定一数组，求a[j]-a[i]最大值。(i<j)<br>
维护最小元素和最大收益就行。。这种题要秒懂啊.<br>
实验证明，用min，max判断比三目运算符要慢。。
```
public int maxProfit(int[] p) {
    if(p.length==0) return 0;
    int min_p=p[0], max_pro=0;
    for(int i=0;i<p.length;i++){
        min_p = min_p > p[i] ? p[i]:min_p;
        max_pro = max_pro < p[i]-min_p ? p[i]-min_p : max_pro;
    }
    return max_pro;
}
```
[198. House Robber](https://leetcode.com/problems/house-robber/description/)<br>
题意：一个正数组，可以取若干元素但不能取相邻元素，求能取的最大值。<br>
自己的解法：动规```ans[i]=max(ans[i-1], nums[i]+max(ans[i-2], ans[i-3]))```， 虽然没错但代码比较繁琐，具体见[这里](https://leetcode.com/problems/house-robber/submissions/1)<br>
别人家的代码！简洁明了，确实思路非常巧妙啊。<br>
考虑奇偶性。
```java
public int rob(int[] nums){
    int len = nums.length;
    int a=0, b=0;
    for(int i=0;i<len;i++){
        if(i%2==0) a = Math.max(a+nums[i], b);
        else b = Math.max(a, b+nums[i]);
    }
    return Math.max(a,b);
}
```
