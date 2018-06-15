
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
