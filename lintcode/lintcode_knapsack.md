当物品可以用多次，而且不一定要求装满背包时，除了V[0]=0外，其他初始化为负无穷。最终结果要取体积0~M中的最大价值。



8/3 [799. Backpack VIII ](https://www.lintcode.com/problem/backpack-viii/description)<br>

给定一系列硬币的面值和数量，问1~n有多少数额能被组成？

为什么啊。。没懂啊

```python
    def backPackVIII(self, n, value, amount):
        # write your code here
        dp = [False for i in range(n + 1)]
        dp[0] = True
        res = 0
        m = len(value)
        for i in range(m):
            cnt = [0 for x in range(n + 1)]
            for j in range(value[i], n + 1):
                if dp[j] == False and dp[j - value[i]] and cnt[j - value[i]] < amount[i]:
                    dp[j] = True
                    res = res + 1
                    cnt[j] = cnt[j - value[i]] + 1         
        return res
```



7/12 [798. Backpack VII-solution](https://www.jiuzhang.com/solution/backpack-vii/#tag-highlight)<br>
题意：给定n元，以及一系列物品的价格price，重量weight，数量amounts，问最多能买多重。

二维伪代码如下：

```java
for (int i = 1; i <= N; ++i) {
    for (int j = 0; j <= V; ++j) {
        backpack[i][j] = backpack[i - 1][j];
        for (int k = 1; k <= num[i]; ++k) {
            if (j >= k * cap[i]) {
                backpack[i][j] = Math.max(backpack[i][j], backpack[i - 1][j - k * cap[i]] + k * val[i]);
            }
        }
    }
}
```

这是一维版本。f[j] = f[j - cap[i]] + val[i] = f[j - 2 * cap[i]] + val[i] + val[i] = .....因此循环语句可以不出现枚举个数的变量。

以下是九章解答。

```python
def backPackVII(self, n, prices, weight, amounts):
    f = [0 for x in range(n + 1)]
    m = len(prices)
    for i in range(m):
        for j in range(1, amounts[i] + 1):
            for k in range(n + 1)[::-1]:# n yuans
                if k >= prices[i]:
                    f[k] = max(f[k], f[k - prices[i]] + weight[i])
    return f[n]
```

**0-1 backpack**

6/19 [564. Combination Sum IV](https://www.lintcode.com/problem/combination-sum-iv/description)<br>
题意：给定不重复的一系列物品体积，问有多少种排列方法可以组成指定target值。 112，121算不同方法。
为啥是先loop背包体积：题目要求排列数，所以应当在一个固定体积下遍历过所有背包的组合情况后，再进入下一个体积。

```Java
public int backPackVI(int[] nums, int m) {
    int[] dp = new int[m + 1];//len = target
    dp[0] = 1;
    for (int j = 1; j < dp.length; j++) { 
	//first loop the backpack volume
        for (int i = 0; i < nums.length; i++) { 
		//then the item index
            if (j - nums[i] >= 0) {
                dp[j] += dp[j - nums[i]];
            }
        }
    }
    return dp[m];
}
```
如果要求方法的不同组合数，像563，那就交换循环次序,先index再volume。

6/19 [563. Backpack V](https://www.lintcode.com/problem/backpack-v/description)<br>
给定n个物品的体积，每种物品用一次，装满指定体积m有多少种方法。<br>

也是01.惊呆了，为什么可以直接累加。。

```java
public int backPackV(int[] A, int m) {
    int n = A.length;
    int [] f = new int[m + 1];
    int i, j;
    f[0] = 1;
    for (i = 1; i <= n; ++i) {
        for (j = m; j >= A[i-1]; --j) {
            f[j] += f[j - A[i - 1]];
        }
    }
    return f[m]; 
}
```

[92. Backpack](https://www.lintcode.com/problem/backpack/description)<br>
给定n个物品的体积，一个背包体积m，求最多能装多少。<br>
[125. Backpack II](https://www.lintcode.com/problem/backpack-ii/description)<br>
给定n个物品的体积和价值，一个背包体积m，求最多能装的价值。<br>

125和92都是01背包。92题的物品没有价值，直接把费用当做价值考虑就行<br>
几个要注意的点：<br>
1 这是01背包，故dp数组的v要从<背包容量值>m往0遍历。<br>
2 因为待选物品的的价值和费用并不按照顺序排列，因此dp需要从<背包容量值>m遍历到0才行。

```java
public int backPack(int m, int[] A, int[] V) {
    int len = A.length;
    int [] dp = new int[m+1];
    for(int i=0; i<len; ++i){
        for(int v=m; v>=0; --v){
            if(v>=A[i]) dp[v] = Math.max(dp[v], dp[v-A[i]] + V[i]);
        }
    }
    return dp[m];
}
```
01背包，v逆序遍历。完全背包，v顺序遍历。希望日后你还能看懂现在的笔记。。。。

如果不要求完全放满背包，那么可以初始化dp都为0。否则，如果要求完全放满，那么只能初始化dp[0]=0,其余为dp[i]=负无穷。

一个简单有效的优化
完全背包问题有一个很简单有效的优化，是这样的：若两件物品i、j 满足Ci <= Cj且Wi >= Wj，则将可以将物品j 直接去掉，不用考虑。
这个优化的正确性是显然的：任何情况下都可将价值小费用高的j 换成物美价廉的i，得到的方案至少不会更差。对于随机生成的数据，这个方法往往会大大减少物品的件数，从而加快速度。然而这个并不能改善最坏情况的复杂度，因为有可能特别设计的数据可以一件物品也去不掉。
这个优化可以简单的O(N2) 地实现，一般都可以承受。另外，针对背包问题而言，比较不错的一种方法是：首先将费用大于V 的物品去掉，然后使用类似计数排序的做法，计算出费用相同的物品中价值最高的是哪个，可以O(V + N) 地完成这个优化。这个不太重要的过程就不给出伪代码了，希望你能独立思考写出伪代码或程序。
