6/23 [202. Happy Number](https://leetcode.com/problems/happy-number/discuss/56917/My-solution-in-C(-O(1)-space-and-no-magic-math-property-involved-))<br>
题意：给定一个数，每次将各个数位平方后求和。问是否最后能到达1。
下面是很妙的做法：从寻找带环链表的思路启发。一个快指针每次走两步，慢指针每次一步。<br>
java version
```
int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }return sum;
}
bool isHappy(int n) {
    int slow, fast;
    slow = fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while(fast !=1 && slow != fast);
    return slow == 1 ? 1 : 0;
}
```
py version
```
def isHappy(self, n):
    if n<=0:
        return False
    slow,fast=n,n
    while fast!=1:
        slow=sum([int(i) ** 2 for i in str(slow)])
        fast=sum([int(i) ** 2 for i in str(fast)])
        fast=sum([int(i) ** 2 for i in str(fast)])
        if slow==fast and fast!=1:
            return False
    return True 
```
哈希做法：
```
public boolean isHappy(int n) {
    Set<Integer> inLoop = new HashSet<Integer>();
    int squareSum,remain;
	while (inLoop.add(n)) {
		squareSum = 0;
		while (n > 0) {
		    remain = n%10;
			squareSum += remain*remain;
			n /= 10;
		}
		if (squareSum == 1)
			return true;
		else
			n = squareSum;
	}
	return false;
}
```
```
def isHappy(self, n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    else:
        return True
```
[292. Nim Game](https://leetcode.com/problems/nim-game/description/)<br>
每次只能取1，2，3个石头。你先取。给定石头数n，问谁会赢。

[598. Range Addition II](https://leetcode.com/problems/range-addition-ii/description/)<br>
不要忘记数组为空的情况！也不要随便把初始值设置成最大值。
最好是能够根据具体样例选择初始值。
```
class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int rmin=m, cmin=n; //蠢货，总是忘记数组为空的情况！
        for(int i=0;i<ops.length;i++){
            rmin=Math.min(rmin, ops[i][0]);
            cmin=Math.min(cmin, ops[i][1]);
        }
        return rmin*cmin;
    }
}
```
