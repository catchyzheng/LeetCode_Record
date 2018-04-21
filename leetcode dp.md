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
自己有动规，但是效率比较低。。看看别人的先[here](https://leetcode.com/problems/predict-the-winner/solution/)<br>

[62. Unique Paths](https://leetcode.com/problems/unique-paths/description/)<br>
入门级别动规<br>
[357. Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/discription/)<br>
感觉和动规没什么关系。。就是一数学题。<br>
[392. isSubsequence](https://leetcode.com/problems/is-subsequence/description/)<br>
常规的双指针做法确实比较慢。**日后看看其他讨论？**<br>
关于如果有大量数据需要比较的，讨论在[这里](https://leetcode.com/problems/is-subsequence/discuss/?page=2)<br>

[647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/solution/)<br>
要知道n方的动规和枚举中心点怎么做？

[338. Counting Bits](https://leetcode.com/problems/counting-bits/description/)<br>
找到指定数的二进制表示中1的个数。
a[n] = a[n/2] + n%2 
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
```
public int numberOfArithmeticSlices(int[] A) {
    int len = A.length;
    if(len==0 || len==1) return 0;
    for(int i=0; i<len-1; i++){
        A[i] = A[i+1]-A[i];
    }
    int [] a = new int[len-1];
    int [] b = new int[len-1];
    a[0]=0; b[0]=1;
	//a[i]代表到i时已经有多少个算数列，b[i]代表在i时已经有连续几个相同数。
    int cnt=0;
    for(int i=1; i<len-1; i++){
        if(A[i]==A[i-1]){
            a[i]=a[i-1]+b[i-1];
            b[i]=b[i-1]+1;
        }
        else{
            a[i]=a[i-1]; b[i]=1; 
            //if use the last element of 'a' to record the answer, 
            //you should at least keep a[i] undescending. 
        }
    }
    return a[a.length-1];
}
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
[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
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
[198. House Robber](https://leetcode.com/problems/house-robber/description/)
题意：一个正数组，可以取若干元素但不能取相邻元素，求能取的最大值。<br>
自己的解法：动规ans[i]=max(ans[i-1], nums[i]+max(ans[i-2], ans[i-3]))， 虽然没错但代码比较繁琐，具体见[这里](https://leetcode.com/problems/house-robber/submissions/1)<br>
别人家的代码！简洁明了，确实思路非常巧妙啊。<br>
```
class Solution {
    public int rob(int[] nums){
        int len = nums.length;
        int a=0, b=0;
        for(int i=0;i<len;i++){
            if(i%2==0) a=Math.max(a+nums[i], b);
            else b.Math.max(a, b+nums[i]);
        }
        return Math.max(a,b);
    }
}
```
