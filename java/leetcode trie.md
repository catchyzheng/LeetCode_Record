8/14 [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/description/)

题意：给定一个单词集合，找到最长的且字典序最小的单词，满足所需条件：abc为结果，a ab abc都在集合中。

方法1：暴力枚举。注意排序的代码，和判断的代码。

```python
class Solution(object):
    def longestWord(self, words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c)) # good
        for word in words:
            if all(word[:k] in wordset for k in xrange(1, len(word))): # good
                return word

        return ""
```

方法2：字典树。