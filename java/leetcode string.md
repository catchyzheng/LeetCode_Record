6/18 [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/description/)<br>
返回在haystack中needle串第一次出现的下标，否则-1.<br>
```
public int strStr(String haystack, String needle) {
    if(haystack=="" || needle=="") return 0;
    int hlen = haystack.length(), nlen = needle.length();
    for(int i=0; i<=hlen-nlen; ++i){
        if (haystack.substring(i,i+nlen).equals(needle)) {
            return i;
        }
    }
    return -1;
}
```
特殊情况：双空串，一空一菲空，长度不一。

6/18 [434. Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/description/)<br>
按照空格分割，问能分割出多少个字符串（块）。<br>
直接统计，前一个字符非空格后一个字符为空格的出现次数就行。。。easy啊
```
public int countSegments(String s) {
    int res=0;
    for(int i=0; i<s.length(); i++)
        if(s.charAt(i)!=' ' && (i==0 || s.charAt(i-1)==' '))
            res++;        
    return res;
}
```
6/18 [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/solution/)<br>
将字符串变成z形。


[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)<br>
找到最长的且没有重复字母的子串。<br>
我的解答，就是最优方法！哈哈哈哈。<br>
```
public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> map = new HashMap<>();
    int ans=0; // length of the temp string slide window. 
    int max_=0;
    int i=0;
    for(int j=0; j<s.length(); j++){
        if(map.containsKey(s.charAt(j))){
            i= Math.max(i, map.get(s.charAt(j)));
            ans=j-i;//sub_s=s.substring(i+1, j+1);
        }
        else{
            ans++;
        }
        map.put(s.charAt(j), j);
        max_ = max_>ans ? max_ : ans;
    }
    return max_;
}
```
其实就是双指针法。初始化i=0为目标ans串的头部下标。从头遍历字符串，如果扫描到出现过的字符，那就将i设置为当前下标和该字符上一个出现的下标这两者的较大值。也就是保证上一个该字符的下标在i后面，也就是i后面都是不重复的字符。

[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8064/My-java-solution-with-FIFO-queue)<br>
手机九宫格按键，给出一串数字，每个数字可以对应多个字母。列出所有字母组合。<br>
下面是用linkedlist做的，BFS,很强。
```
public List<String> letterCombinations(String digits) {
	LinkedList<String> ans = new LinkedList<String>();
	if(digits.isEmpty()) return ans;
	String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
	ans.add("");//initial
	for(int i =0; i<digits.length();i++){
	    int x = Character.getNumericValue(digits.charAt(i));
	    while(ans.peek().length()==i){
	        String t = ans.remove();//obtain the peek and then delete
	        for(char s : mapping[x].toCharArray())
	            ans.add(t+s);// equals to addLast
	    }
	}
	return ans;
}
```
扫描数字串。每扫描到一个数字，就将对应的字母加在list头部的字符串元素末尾，组成新串，依次add到list中。然后下一个数字重复。直到扫描到数字串末尾。这是很新奇的思路！

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
自己的思路就是根据空格split然后返回最后一个str的长度。但其实不用split，只要**从末尾往前扫描**就可以统计出答案了。
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