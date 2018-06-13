6/13 []()<br>
计算两个集合的交集，包含重复元素。可以有二分和非二分的做法。<br>
非二分做法：先对两集合分别排序。用两个下标指针，依次比较两个下标指向的元素的大小，元素小的指针自增1.如果相等，就加入ans数组中。

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
