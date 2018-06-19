6/19 [514. Paint Fence](https://www.lintcode.com/problem/paint-fence/description)<br>
lintcode：用k个颜色给n个并排的桩着色，最多只能连续两个同色。求方法个数。
```
```<br>
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

其实，假设房子总数为n，那么就分别对1~(n-1)和2~n的房子看做直线排列看待。

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