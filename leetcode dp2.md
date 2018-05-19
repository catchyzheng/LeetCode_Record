[](https://leetcode.com/problems/house-robber-ii)<br>

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