[13. Roman to Integer]()<br>
罗马数字转十进制。
一些让代码提速的小trick。比如用switch函数代替map，以及sync_with_stdio(false)。[了解一下](https://leetcode.com/submissions/detail/150864113/)

[14. Longest Common Prefix](https://leetcode.com/submissions/detail/150934134/)<br>
找出所有字符串的最长公共前缀。beats 74%。
```
public String longestCommonPrefix(String[] strs) {
    int len = strs.length;
    if(len==0) return "";
    int minlen=10000;
    for(String s: strs) minlen = minlen < s.length() ? minlen:s.length();
    int cnt=0;
    boolean cannot=false;
    while(cnt<minlen){
        char c = strs[0].charAt(cnt);
        for(int i=0; i<len; i++){
            if(c!=strs[i].charAt(cnt)) {cannot=true; break; }
        }
        if(!cannot) cnt++;
        if(cannot) break;
    }
    return strs[len-1].substring(0,cnt);
}
```

[58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/submissions/1)<br>
**注意，输入的字符串末尾可以有空白。**
自己的思路就是根据空格split然后返回最后一个str的长度。但其实不用split，只要从末尾往前扫描就可以统计出答案了。
```
public int lengthOfLastWord(String s) {
    int len=s.length(), lastLength=0;
    while(len > 0 && s.charAt(len-1)==' '){
        len--;
    }
    while(len > 0 && s.charAt(len-1)!=' '){
        lastLength++;
        len--;
    }
    return lastLength;
}
```