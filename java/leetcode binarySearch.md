
6/15 [475. Heaters](https://leetcode.com/problems/heaters/description/)<br>
给定一系列房子的一维位置和一系列火炉的位置，求要让火炉覆盖所有房子的最小半径。<br>
简言之，要让所有等半径的圆覆盖所有点。
<br>
Arrays自带的binarySearch: <br>
1、如果找到关键字，则返回关键字在数组中的位置，从0开始<br>
2、如果没有找到关键字，返回负的插入点值.所谓插入点值就是第一个比关键字大的元素在数组中的位置索引，从1开始。<br>
和答案思路一致，但是忘记了一个重要条件。
别人家的代码总是没有让我失望过。。
```
public int findRadius(int[] houses, int[] heaters) {
    Arrays.sort(heaters);
    int result = Integer.MIN_VALUE;
    
    for (int house : houses) {
        int index = Arrays.binarySearch(heaters, house);
        if (index < 0) {
    	index = -(index + 1); //return neg
        }
        int dist1 = index - 1 >= 0 ? house - heaters[index - 1] : Integer.MAX_VALUE;
        int dist2 = index < heaters.length ? heaters[index] - house : Integer.MAX_VALUE;
    
        result = Math.max(result, Math.min(dist1, dist2));
    }
    
    return result;
}
```
重要条件：先要对火炉位置从小到大排序。

6/15 [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)<br>
在一个数组中寻找目标值。如果找不到，就寻找应该被插入的下标位置。<br>
基本二分法。照着模板就行啦====
```
public int searchInsert(int[] nums, int target) {
    if(target<nums[0]) return 0;
    if(target>nums[nums.length-1]) return nums.length;
    int low = 0, high = nums.length-1, mid;
    while(low < high){
        mid = low + (high - low)/2;
        if(target==nums[mid]) {low = mid; break; }
        if(nums[mid]>target) high = mid;
        else low = mid+1;
    }
    return low;
}
```
6/15 [69. Sqrt(x)](https://leetcode.com/playground/new)<br>
二分法找平方根。注意x是非负整数！！<br>
6/15 [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/description/)<br>
常规二分。依然是对low = mid + 1。
```
public int guessNumber(int n) {
    int low = 1, high = n, mid;
    while(low<high){
        mid = low + (high - low)/2;
        if(guess(mid)==0) {low = mid; break; }
        else if(guess(mid)==1) low=mid+1;
        else high=mid;
    }
    return low;
}
```
下一题：[375. Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/)<br>
题意不清。。。

6/15 [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/description/)<br>
判断一个数是否是平方数。<br>
坑点1：要用long，不然会overflow。
坑点2：特殊判断n=1. 这是自己考虑不周所致。
```
public boolean isPerfectSquare(int num) {
    if(num==1) return true;
    long low = 1, high = num, mid;
    boolean can = false;
    while(low < high){
        mid = low + (high - low)/2;
        if(mid*mid == num) { can=true; break; } 
        else if(mid*mid < num) low = mid+1;
        else high = mid;
    }
    return can;
}
```

6/14 [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/)<br>
给定一系列程序版本的编号，找到最先错误的版本号。<br>
二分查找基本功。要注意low+（high-low）/2.否则会溢出。以及更新low和high时候只有一个需要+1.<br>
```
public int firstBadVersion(int n) {
    if(isBadVersion(1)) return 1;
    int low=1, high=n;
    int mid;
    while(low<high){
        mid=low + (high - low)/2;
        if(isBadVersion(mid)) high=mid;
        else low=mid+1;
    }
    return low;
}
```

6/14 [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)<br>
计算两个集合的交集，包含重复元素。可以有二分和非二分的做法。<br>
非二分做法：先对两集合分别排序。用两个下标指针，依次比较两个下标指向的元素的大小，元素小的指针自增1.如果相等，就加入ans数组中。<br>
二分做法：对集合b的元素，依次在集合a中进行二分查找。<br>
```
public int[] intersect(int[] nums1, int[] nums2) {
    Arrays.sort(nums1);
    Arrays.sort(nums2);
    int i=0, j=0;
    List<Integer> ans = new ArrayList<>();
    while(i<nums1.length && j<nums2.length){
        if(nums1[i] < nums2[j]) i++;
        else if(nums2[j] < nums1[i]) j++;
        else {
            ans.add(nums1[i]);
            i++; j++; 
        }
    }
    int [] result = new int[ans.size()];
    int k=0;
    for(int ele: ans){
        result[k++]=ele;
    }
    return result;
}
```

5/30 [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)<br>
超级简单的二分法练手。。
```
public int searchInsert(int[] nums, int target) {
    int l=0, r=nums.length-1;
    if(target>nums[r]) return r+1;
    if(target<nums[l]) return 0;
    int m;
    while(l<r-1){
        m=(l+r)/2;
        if(nums[m]==target) return m;
        else if(nums[m]>target){
            r=m;
        }
        else l=m;
    }
    if(nums[l]==target) return l;
    else return l+1;
}
```
5/29 [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)
二分还是分治，或是兼而有之？
我是先尝试收缩行列的各自上下界，然后直接遍历查找。。效率不高。日后看看discuss的方法
