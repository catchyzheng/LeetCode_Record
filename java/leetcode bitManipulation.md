5/24 [389. Find the Difference]()<br>
这题。。其实是不允许使用任何java容器的，“XXX is not declared in this scope.”<br>
日后自己想一想，怎么做才是最快的？<Br>
其实有个隐含情况，那就是加的字母曾经出现在原字符串中。<br>
这时候你还会想用set吗。
```
public char findTheDifference(String s, String t) {
    int a=0;
    for(char c: s.toCharArray()) a^=c-'a';
    for(char d: t.toCharArray()) a^=d-'a';
    return (char)(a+'a');
}
```

5/23 [260. Single Number III](https://leetcode.com/problems/single-number-iii//description/)<br>
题意：除了两个数仅有一次，其他每个数都出现了两次。找到那两个数。<br>
其实一直没懂的是，为何取了全部数XOR后结果的最后一位后，就可以根据这个最后一位来分出两组数，每组数必定包含一个仅出现一次的数？

5/20 [137. Single Number II](https://leetcode.com/problems/single-number-ii/description/)<br>
题意：除了一个数仅有一次，其他每个数都出现了三次。找到那个数。
其实就是参考下面的文章的做法。。

[关于single number问题的解释和泛化。](https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers)<br>
Given an array of integers, every element appears k (k > 1) times except for one, which appears p times (p >= 1, p % k != 0). Find that single one."<br>

[A summary: how to use bit manipulation to solve problems easily and efficiently](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)<br>
唉水平太差了，没怎么看懂。。只看出各种问题的不同解法，但好像没有什么规律可循。。

[461. Hamming Distance](https://leetcode.com/problems/hamming-distance/description/)<br>

[136. Single Number](https://leetcode.com/problems/single-number/description/)<br>
找到只出现一次的数。
直接全部XOR。

[762. Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/)<br>
唉，感觉有了Integer.bitCount()一切都变得无脑。。但这是不对的。

[338. Counting Bits](https://leetcode.com/problems/counting-bits/description/)<br>
给定n，返回0-n依次的1比特数。

[191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/description/)<br>

[231. Power of Two](https://leetcode.com/problems/power-of-two/description/)<br>

