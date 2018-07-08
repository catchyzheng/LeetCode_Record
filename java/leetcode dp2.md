7/7 [416. Partition Equal Subset Sum](https://leetcode.com/problems/longest-valid-parentheses/description/)<br>
题意：给定一个非空的正整数组，问是否能够分成两块，使得和相同。<br>
其实嘛。。很简单的动规模板题。看看你能不能回想起来用什么模板了。
```
public boolean canPartition(int[] nums) {
    int len = nums.length;
    int total = 0;
    for(int num: nums) total += num;
    if(total % 2!=0) return false;
    int [] dp = new int[total/2+1];
    for(int i=0; i<len; ++i){
        for(int j=total/2; j>=0; --j){
            if(j >= nums[i]) dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);
        }
    }
    return dp[total/2] == total/2 ? true: false;
}
```

7/4 [376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/description/)<br>
题意：给定一个序列，求最长的子序列，使得相邻元素的差呈正负交替。序列不一定要连续，但元素相对位置要相同。<br>
解法，典型动规，用两个数组表示以当前下标结尾的最长子序列。
妈的。。好多次WA。。。
```
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int down = 1, up = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1])
                up = down + 1;
            else if (nums[i] < nums[i - 1])
                down = up + 1;
        }
        return Math.max(down, up);
    }
}
```
特殊情况：【3，3，3，2，2，5，5】

7/2 [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/description/)<br>
题意：给定一序列不相同的正整数，求最大的子集，使得任意两个数字都是倍数关系。<br>

```
public List<Integer> largestDivisibleSubset(int[] nums) {
    int n = nums.length;
    int[] count = new int[n];
    int[] pre = new int[n];
    Arrays.sort(nums);
    int max = 0, index = -1;
    for (int i = 0; i < n; i++) {
        count[i] = 1;
        pre[i] = -1;
        for (int j = i - 1; j >= 0; j--) {
            if (nums[i] % nums[j] == 0) {
                if (1 + count[j] > count[i]) {
                    count[i] = count[j] + 1;
                    pre[i] = j;
                }
            }
        }
        if (count[i] > max) {
            max = count[i];
            index = i;
        }
    }
    List<Integer> res = new ArrayList<>();
    while (index != -1) {
        res.add(nums[index]);
        index = pre[index];
    }
    return res;
}
```
思路不难动规，但1要输出路径，因此采用pre数组记录上一个下标。2

7/1 [139. Word Break](https://leetcode.com/problems/word-break/description/)<br>
题意：给定一个长字符串和一系列短串，问长串是否能由短串构成。短串可以使用无限次。<br>
想想看，什么思想什么解法？
```
public boolean wordBreak(String s, Set<String> dict) {
    boolean[] f = new boolean[s.length() + 1];
    f[0] = true;
    /*//First DP
    for(int i = 1; i <= s.length(); i++){
        for(String str: dict){
            if(str.length() <= i){
                if(f[i - str.length()]){
                    if(s.substring(i-str.length(), i).equals(str)){
                        f[i] = true;
                        break;
                    }
                }
            }
        }
    }//*/
    //Second DP
    for(int i=1; i <= s.length(); i++){
        for(int j=0; j < i; j++){
            if(f[j] && dict.contains(s.substring(j, i))){
                f[i] = true;
                break;
            }
        }
    }//*/
    return f[s.length()];
}
```


6/19 [514. Paint Fence](https://www.lintcode.com/problem/paint-fence/description)<br>
lintcode：用k个颜色给n个并排的桩着色，最多只能连续两个同色。求方法个数。<br>
```
```
[详细讲解链接](http://yuanhsh.iteye.com/blog/2219891)
![image](http://m.qpic.cn/psb?/V13hu9k31D6BsB/h2fPxNVtSg.4zygk0nvtca6QSIRL1sikkXl4ihg6f9s!/b/dFkAAAAAAAAA&bo=dgO5AQAAAAARF.0!&rf=viewer_4&t=5)
第i根柱子要么和i-1颜色不一样，要么和i-1颜色相同但和i-2颜色不一样。不一样的颜色选择有k-1种。
p[i] = (p[i-1]+p[i-2])*(k-1);


[Most-consistent-ways-of-dealing-with-the-series-of-stock-problems](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems)<br>
5.26再次研读感想：<br>
作者的代码中有几个值得思考的地方：
(1)遍历的顺序。在Case IV交易数为任意K的情况下，应选择外层循环正序遍历price，内层循环逆序遍历k。从Case III的代码中可看出，逆序遍历才是符合理论依据的，在同个循环中后面的式子不会用到前面式子的更新值。
```
for (int price : prices) {
    T_i20 = Math.max(T_i20, T_i21 + price);
    T_i21 = Math.max(T_i21, T_i10 - price);
    T_i10 = Math.max(T_i10, T_i11 + price);
    T_i11 = Math.max(T_i11, -price);
}
```
(2)在Case VI含交易费的情景下，交易费在哪个公式扣除，有讲究的。要看初始值，在solution2里，因为T_ik1初始化为负无穷，因此T_ik1 + price - fee在fee > price情况下会溢出。因而要特别处理溢出情况。<br>
(3)作者假设，仅在买动作发生时候改变最大交易次数。这是为了代码上处理边界条件方便而做出的假设。实际上在卖动作改变也行，但复杂些。<br>
这篇文章将所有有关股票交易的题目都放在了一个大的框架下阐述。事实证明，每道题其实都是由这个大框架衍生出来的一些特例或者变体。清晰明白，讲解透彻，学到了很多！<br>
感觉，表示收益的T数组在初始化时候，如果手中没有股票就都是初始化为0，有股票就初始化为负无穷。<br>
看完之后，受益匪浅！曾经看不懂的transaction with cool down，在作者的通用框架下只需小小的改动！非常佩服作者这样找到若干特殊问题背后的一般规律的人。仿佛统一了经典力学和量子力学。（好吧我是物理渣）

[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/kadanes-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input)<br>
一个121的变体：如果给出的数组不是每天的价格，而是当天价格减去前一天价格的差，那么要怎么求解？<br>
虽然没听过kadane算法。。但这篇的思路还是挺不错的。确实类似最大子数组问题。依次累加当天价格和前一天价格的差。如果小于零了就置零。同时维护最大累加和。
```
public int maxProfit(int[] prices) {
    int maxCur = 0, maxSoFar = 0;
    for(int i = 1; i < prices.length; i++) {
        maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
        maxSoFar = Math.max(maxCur, maxSoFar);
    }
    return maxSoFar;
}
```
[213. House Robber II](https://leetcode.com/problems/house-robber-ii)<br>
版本一是房子成一条线，版本二是房子围成圆圈。其他要求不变，不能抢劫相邻房子。

其实，假设房子总数为n，那么就分别对1至(n-1)和2至n的房子看做直线排列看待。

[322. Coin Change](https://leetcode.com/problems/coin-change/description/)<br>
给定一序列硬币面值和一个目标值，求组成目标值需要的最少硬币个数。硬币可以拿无限个。<br>
典型动规。。动规的方程不难想到。但边界条件的处理比较关键。
```
public int coinChange(int[] coins, int amount) {
    if(amount == 0) return 0;
    int [] dp = new int[amount+1];
    for(int i=1; i<=amount; ++i) dp[i]=Integer.MAX_VALUE-1;
    dp[0]=0;
    for(int i=0;i<=amount;++i){
        for(int j=0;j<coins.length;++j){
            if(i>=coins[j]) dp[i] = Math.min(dp[i], dp[i-coins[j]] + 1); 
        }
    }
    if(dp[amount]==Integer.MAX_VALUE-1) return -1;
    else return dp[amount];
}
```
答案中，是把dp数组全部初始化为amount+1，以及dp[0]=0。