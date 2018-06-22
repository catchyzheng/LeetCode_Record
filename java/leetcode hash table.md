6/21 [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)<br>
从左到右找到字符串中出现仅一次的字符。
答案：很皮很皮，李时珍皮。不过这仅对字母有用，如果是数字符号都有的话，还是hashmap好了。
```
public int firstUniqChar(String s) {
    int freq [] = new int[26];
    for(int i = 0; i < s.length(); i ++)
        freq [s.charAt(i) - 'a'] ++;
    for(int i = 0; i < s.length(); i ++)
        if(freq [s.charAt(i) - 'a'] == 1)
            return i;
    return -1;
}
```

[136. Single Number](https://leetcode.com/problems/single-number/description/)<br>
找出一个数组中仅出现一次的数。
这段python代码有点迷。。暂时不清楚怎么hash的。。
```
def singleNumber(self, nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]
```
