当物品可以用多次，而且一定要求装满背包时，**除了V[0]=0外，其他初始化为负无穷。**

(不一定的)**最终结果要取体积0~M中的最大价值。**

难题三连：798 799 800

8/3 [799. Backpack VIII ](https://www.lintcode.com/problem/backpack-viii/description)<br>

给定一系列硬币的面值和数量，问1~n有多少数额能被组成？

为什么啊。。没懂啊

```python
def backPackVIII(self, n, value, amount):
    # write your code here
    dp = [False for i in range(n + 1)]
    dp[0] = True
    res = 0
    l = len(value)
    for i in range(l):
        cnt = [0 for x in range(n + 1)]
        for j in range(value[i], n + 1):
            if dp[j] == False and dp[j - value[i]] and cnt[j - value[i]] < amount[i]:
                dp[j] = True
                res = res + 1
                cnt[j] = cnt[j - value[i]] + 1         
    return res
```



7/12 [798. 背包问题VII ](https://www.lintcode.com/problem/backpack-vii/description)

题意：给定n元，以及一系列物品的价格price，重量weight，数量amounts，问最多能买多重。

 [here-798. Backpack VII-solution](https://www.jiuzhang.com/solution/backpack-vii/#tag-highlight)<br>

多重背包问题。二维伪代码如下：

```java
for (int i = 1; i <= N; ++i) {
    for (int j = 0; j <= V; ++j) { //j,k的先后有讲究
        backpack[i][j] = backpack[i - 1][j];
        for (int k = 1; k <= num[i]; ++k) { //j,k的先后有讲究。
            if (j >= k * cap[i]) {
                backpack[i][j] = Math.max(backpack[i][j], backpack[i - 1][j - k * cap[i]] + k * val[i]);
            }
        }
    }
}
```

这是一维版本。f[j] = f[j - cap[i]] + val[i] = f[j - 2 * cap[i]] + val[i] + val[i] = .....因此循环语句可以不出现枚举个数的变量k。

以下是九章解答。

```python
def backPackVII(self, n, prices, weight, amounts):
    f = [0 for x in range(n + 1)]
    m = len(prices)
    for i in range(m):
        for k in range(1, amounts[i] + 1):
            for j in range(n + 1)[::-1]:# n yuans，此为体积。
                if j >= prices[i]:
                    f[j] = max(f[j], f[j - prices[i]] + weight[i])
    return f[n]
```

[800. 背包问题 IX](https://www.lintcode.com/problem/backpack-ix/description?_from=ladder)

你总共有`10 * n` 千元(`n`万元 )，希望申请国外的大学，要申请的话需要交一定的申请费用，给出每个大学的申请费用以及你得到这个大学offer的成功概率，大学的数量是 `m`。如果经济条件允许，你可以申请多所大学。找到获得至少一份工作的最高可能性。

唉。。不懂概率噜。初始化f全为100%，然后f[j] = min(f[j - prices[i]] * (1.0 - probability[i]), f[j])。 因为是01背包，所以要逆序遍历j。

```python
    def backpackIX(self, n, prices, probability):
        # write your code here
        if prices == None or len(prices) == 0:
            return 0.0
        
        f = [1.0] * (n + 1)
        
        for i in range(len(prices)):
            for j in range(n, prices[i] - 1, -1):
                f[j] = min(f[j - prices[i]] * (1.0 - probability[i]), f[j])
        
        return 1.0 - f[n]
```



[801. 背包问题X](https://www.lintcode.com/problem/backpack-x/description?_from=ladder)

有`n`元，商人总共有三种商品，它们的价格分别是150元,250元,350元，三种商品的数量可以认为是无限多的，购买完商品以后需要将剩下的钱给商人作为小费，求`最少`需要给商人多少小费。容易的不行。。

[440. 背包问题 III](https://www.lintcode.com/problem/backpack-iii/description?_from=ladder)

给定n种具有大小 `Ai` 和价值 `Vi` 的物品(`每个物品可以取用无限次`)和一个大小为 `m` 的一个背包, 你可以放入背包里的最大价值是多少?   **包不一定要放满。**那就正常初始化数组为0呀！

[562. 背包问题 IV](https://www.lintcode.com/problem/backpack-iv/description)

题意：给出 n 个物品, 以及一个数组, `nums[i]`代表第i个物品的大小, 保证大小均为正数并且没有重复, 正整数 `target` 表示背包的大小, 找到能填满背包的方案数。 每一个物品可以使用无数次。完全背包无疑了。

注意当体积为零时，方案数为1.

```java
public class Solution {
    /**
     * @param nums: an integer array and all positive numbers, no duplicates
     * @param target: An integer
     * @return: An integer
     */
    public int backPackIV(int[] nums, int m) {
        int len = nums.length;
        int [] dp = new int[m+1];
        dp[0]=1;
        for(int i=0; i<len; ++i){
            for(int j=1; j<=m; ++j){
                if(j>=nums[i]) dp[j] += dp[j-nums[i]];
            }
        }
        return dp[m];
    }
}
```

6/19 [564. Combination Sum IV](https://www.lintcode.com/problem/combination-sum-iv/description)<br>
题意：给定不重复的一系列物品体积，问有多少种排列方法可以组成指定target值。 112，121算不同方法。

例子：给出 nums = `[1, 2, 4]`, target = `4`
可能的所有组合有：

```
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[4]
```

返回 `6`

此题为完全背包。**为啥是先loop背包体积：题目要求排列数，所以应当在一个固定体积下遍历过所有背包的组合情况后，再进入下一个体积**。

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

01背包。惊呆了，为什么可以直接累加。。

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
2 （这条好像不太对）因为待选物品的的价值和费用并不按照顺序排列，因此dp需要从<背包容量值>m遍历到0才行。

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
这个优化可以简单的O(N2) 地实现，一般都可以承受。另外，针对背包问题而言，比较不错的一种方法是：**首先将费用大于V 的物品去掉，然后使用类似计数排序的做法，计算出费用相同的物品中价值最高的是哪个**，可以O(V + N) 地完成这个优化。这个不太重要的过程就不给出伪代码了，希望你能独立思考写出伪代码或程序。
