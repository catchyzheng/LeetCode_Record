[9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)<br>
判断一个数是否回文。负数都不回文。除了0以外的10的倍数也不回文。<br>
看具体算法的思路的耗时才靠谱，而不是看排行榜。有时同样的代码耗时也不一样。<br>
下面的这个代码，可以减少正常人一半的运算。
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

