取石子游戏：两个人轮流取2，3，或5个石子，取到最后一个石头的人获胜。

```python
dp[i] = ! (dp[i-2] and dp[i-3] and dp[i-5])
```

follow up: 多堆石子

[395. Coins in a Line II ](https://www.lintcode.com/problem/coins-in-a-line-ii/description) 

两个人从**右端**每次取1或2个硬币，问最后先手是否能比后手的硬币有更多价值。

```python
dp[i] = sum[i] - min(dp[i-1], dp[i-2]) # 从右端
```

这里的dp[i]表示的是从0-i，先手能取到的最多面值。

两人从任一端每次取1个硬币。

```python
dp[i][j] = sum[i][j] - min(dp[i+1][j], dp[i][j-1]) #左端i右端j
```

follow up: coins in multiple lines. 