5/27 [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/description/)<br>
先横向翻转，然后再01逆。应该要能一次二重循环搞定！
```
public int[][] flipAndInvertImage(int[][] A) {
    int C = A[0].length;
    for (int[] row: A)
        for (int i = 0; i < (C + 1) / 2; ++i) {
            int tmp = row[i] ^ 1;
            row[i] = row[C - 1 - i] ^ 1;
            row[C - 1 - i] = tmp;
        }
    return A;
}
```

5/22 [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)<br>
给定一数组，返回一个数组，每个元素都是除了本身以外的所有元素的乘积。
不难。就是有些坑点。哪里有坑呢？想一想
```
public int[] productExceptSelf(int[] nums) {
    int all = 1;
    int cntZero=0;
    for(int num: nums){
        if(num!=0) all*=num;
        else cntZero++;
    }
    int [] ans = new int[nums.length];
    if(cntZero > 1) return ans;
    else if(cntZero==1){
        for(int i=0; i<nums.length; ++i){
            if(nums[i]==0) ans[i]=all;
        }
    }
    else{
		for(int i=0; i<nums.length; ++i) 
			ans[i] = all/nums[i];
	}
    return ans;
}
```
坑点：1个0和2个以上0的情况。

[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)<br>
给定一系列间隔为1的木板及其长度，任意选择两块木板，求可以达到的最大包围面积。|_|
考虑一个问题：若已知两块木板位置，下一个时刻应该如何移动木板？

[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)<br>
合并两个有序数组，要求合并后的结果存放在nums1中。
想法不难，难就难在如何不新建辅助数组也能合并？下面的代码也许可以给你点启发。
```
public void merge(int[] nums1, int m, int[] nums2, int n) {
    int i = m - 1;
    int j = n - 1;
    for (int k = m + n - 1; k >= 0; k--) {
        if (i < 0) {
            nums1[k] = nums2[j--];
            continue;
        }
        if (j < 0) {
            nums1[k] = nums1[i--];
            continue;
        }
        if (nums1[i] >= nums2[j]) {
            nums1[k] = nums1[i--];
        } else {
            nums1[k] = nums2[j--];
        }
    }
}
```
其实基本思想就是，既然num1的前面都已经存放了元素，那就从最末尾考虑，从大到小归并。这样就算当前访问下标对应的num1位置有元素，那也已经是复制过了的。

[287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/solution/)<br>
一个n+1长的数列中，元素都来自1-n。找到重复的那个数。
方法一：排序。Arrays.sort(nums); 复杂度nlogn。<br>
方法二：set。复杂度n。也可以map。大同小异。**这个方法最适合我**。<br>
其实题目要求是小于n^2时间复杂度，且空间复杂度O(1)。。。那是一个比较神奇的算法。<br>
```
public int findDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<Integer>();
    for (int num : nums) {
        if (seen.contains(num)) { return num;}
        seen.add(num);
    }
    return -1;
}
```
[167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)<br>
一个升序列，给定一个值，找到和为这个值的两个元素的下标。
```
class Solution {
    public int[] twoSum(int[] num, int target) {
        int i=0, j=num.length-1;
        while(i<j){
            int b = target-num[i];
            if(b==num[j]) {break; }
            if(b>num[j]) i++;
            else j--;
        }
        return new int[]{i+1,j+1};
    }
}
```
[1. Two Sum](https://leetcode.com/problems/two-sum/description/)<br>
给一个数组和一个目标值，尝试寻找两个数使得和等于目标值，返回两个数的下标。如果没有，返回空数组。<br>

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        int[] candi = new int[len];
        HashMap<Integer, Integer> map = new HashMap();
        for(int i=0;i<len;i++){
            candi[i] = target - nums[i];
            map.put(candi[i], i);
        }
        for(int j=0;j<len;j++){
            if(map.containsKey(nums[j]) && map.get(nums[j])!=j){
                return new int [] {j, map.get(nums[j])};
            }
        }
        return new int [2];
    }
}
```
附，后台主函数程序代码，值得读读看。
```
public class MainClass {
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
          return new int[0];
        }
    
        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for(int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }
    
    public static String integerArrayToString(int[] nums, int length) {
        if (length == 0) {
            return "[]";
        }
    
        String result = "";
        for(int index = 0; index < length; index++) {
            int number = nums[index];
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }
    
    public static String integerArrayToString(int[] nums) {
        return integerArrayToString(nums, nums.length);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);
            line = in.readLine();
            int target = Integer.parseInt(line);
            
            int[] ret = new Solution().twoSum(nums, target);
            
            String out = integerArrayToString(ret);
            
            System.out.print(out);
        }
    }
}
```