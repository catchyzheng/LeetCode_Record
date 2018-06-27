6/26 [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)<br>

6/24 [204. Count Primes](https://leetcode.com/problems/count-primes/description/)<br>
题意：求小于n的质数的个数。注意，1不是质数，2是。
素数筛选法就行。

6/24 [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)<br>
题意：给出一组字符串，将它们聚集成几个组，每个组的每个字符串都是由相同数量和种类的字母构成。<br>
经典样例解答：就是对每个字符串排序后，添加到指定list中。主要是以下代码的map结构用的好。
```
public List<List<String>> groupAnagrams(String[] strs) {
    if (strs == null || strs.length == 0) return new ArrayList<List<String>>();
    Map<String, List<String>> map = new HashMap<String, List<String>>();
    for (String s : strs) {
        char[] ca = s.toCharArray();
        Arrays.sort(ca);
        String keyStr = String.valueOf(ca);
        if (!map.containsKey(keyStr)) map.put(keyStr, new ArrayList<String>());
        map.get(keyStr).add(s);
    }
    return new ArrayList<List<String>>(map.values());
}
```
神一般的用质数。。基本规律就是，若两个字符串不属于同一组，那么它们转化成的质数乘积也必然不一样。
```
public static List<List<String>> groupAnagrams(String[] strs) { 
   int[] prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};//最多10609个z
    List<List<String>> res = new ArrayList<>();
    HashMap<Integer, Integer> map = new HashMap<>();
    for (String s : strs) {
        int key = 1;
        for (char c : s.toCharArray()) {
            key *= prime[c - 'a'];
        }
        List<String> t;
        if (map.containsKey(key)) {
            t = res.get(map.get(key));
        } else {
            t = new ArrayList<>();
            res.add(t);
            map.put(key, res.size() - 1);
        }
        t.add(s);
    }
    return res;
}
```
my code's efficiency is not good, only 29%.
```
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, String> map = new HashMap<>();
    Set<String> set = new HashSet<>();
    //
    for(String str: strs){
        char [] chars = str.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        map.put(str, sorted);
        set.add(sorted);
    }
    //
    List<List<String>> res = new ArrayList<>();
    Map<String, Integer> s2i = new HashMap<>();
    int i=0;
    for(String s: set){
        List<String> temp = new ArrayList<>();
        //temp.add(s);
        res.add(temp); s2i.put(s, i++);
    }
    for(String str: strs){
        res.get(s2i.get(map.get(str))).add(str);
    }
    return res;
}
```

follow up:
[217. Contains Duplicate]() [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/description/)
6/23 [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/)<br>
题意：给定一数组和一个k，问是否能找到两个不同下标，使得对应的元素值相同，且下标差距不超过k。<br>
```
public boolean containsNearbyDuplicate(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap();
    for(int i=0; i<nums.length; ++i){
        if(map.containsKey(nums[i]) && map.get(nums[i])>0 && (i+1-map.get(nums[i])) <= k) return true;
        map.put(nums[i], i+1);
    }
    return false;
}
```
解法，用一个hashmap遍历整个数组，每次的存储以访问元素为键，下标+1为值。判断当前下标和哈希表中的对应键值是否差小于k。


6/22 [290. Word Pattern](https://leetcode.com/problems/word-pattern/description/)<br>
规则类似isomorphic string，只不过将其中一个字符数组改成字符串数组。

原来for循环中循环变量Integer和int有差别啊。。。
```
public boolean wordPattern(String pattern, String str) {
    String[] words = str.split(" ");
    if (words.length != pattern.length())
        return false;
    Map index = new HashMap<>();
    for (Integer i=0; i<words.length; ++i)
        if (index.put(pattern.charAt(i), i) != index.put(words[i], i))
            return false;
    return true;
}
```
```
public boolean wordPattern(String pattern, String str) {
    String[] arr= str.split(" ");
    HashMap<Character, String> map = new HashMap<Character, String>();
    if(arr.length!= pattern.length())
        return false;
    for(int i=0; i<arr.length; i++){
        char c = pattern.charAt(i);
        if(map.containsKey(c)){
            if(!map.get(c).equals(arr[i]))
                return false;
        }else{
            if(map.containsValue(arr[i]))
                return false;
            map.put(c, arr[i]);
        }    
    }
    return true;
}
```

py解答，日后看这里[here](https://leetcode.com/problems/word-pattern/discuss/73433/Short-in-Python)<br>

6/22 [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)<br>
题目：判断两个单词是否有一样的相对结构，即1213，对应2324或者1215。一个字符可以映射到自己本身。<br>
感觉，字符串题目还是c++写起来方便啊。。
```
bool isIsomorphic(string s, string t) {
    int m1[256] = {0}, m2[256] = {0}, n = s.size();
    for (int i = 0; i < n; ++i) {
        if (m1[s[i]] != m2[t[i]]) return false;
        m1[s[i]] = i + 1;
        m2[t[i]] = i + 1;
    }
    return true;
}
```

6/21 [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)<br>
从左到右找到字符串中出现仅一次的字符。
不是自己的答案：很皮很皮，李时珍皮。不过这仅对字母有用，如果是数字符号都有的话，还是hashmap好了。
```
public int firstUniqChar(String s) {
    int freq[] = new int[26];
    for(int i = 0; i < s.length(); ++i)
        freq[s.charAt(i) - 'a'] ++;
    for(int i = 0; i < s.length(); ++i)
        if(freq[s.charAt(i) - 'a'] == 1)
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
