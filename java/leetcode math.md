6/14 [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/description/)<br>
解方程：（k+1）*k/2 <= n，k是未知数。
sqrt里面要用小数。。。好吧。
```
    public int arrangeCoins(int n) {
        return (int)((Math.sqrt(1+8.0*n)-1)/2.0);
    }
```
5/19 [258. Add Digits](https://leetcode.com/problems/add-digits/description/)<br>
感觉数学题并不能体现编程能力orz。。。<br>
Follow up:Could you do it without any loop/recursion in O(1) runtime?

[9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)<br>
判断一个数是否回文。负数都不回文。除了0以外的10的倍数也不回文。<br>
看具体算法的思路的耗时才靠谱，而不是看排行榜。有时同样的代码耗时也不一样。<br>
自己的代码。
```
public boolean isPalindrome(int x) {
    if(x==0) return true;
    int n=0, y=x;
    while(y>0){
        n=n*10+y%10;
        y/=10;
    }
    if(x==n) return true;
    else return false;
}
```
下面的这个代码，可以减少正常人一半的运算。因为只是反转了一半的长度。
```
public bool IsPalindrome(int x) {
    if(x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }
    int rn = 0;
    while(x > rn) {
        rn = rn * 10 + x % 10;
        x /= 10;
    }
    return x == rn || x == rn/10;
    }
```

