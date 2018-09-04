二分法做题的若干细节，无需言传，意会便知：<br>

1 mid = low + (high - low)/2;<br>
2 low = mid+1;<br>
3 int long的越界问题。<br>
4 注意搜索空间是值范围还是下标范围。
7/8 [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation):-O(nlog(n)-and-O(n)-time-O(1)-space-without-changing-the-input-array)<br>

Given an array *nums* containing *n* + 1 integers where each integer is between 1 and *n* (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

用二分也是可以做的。注意，这里的搜索空间是值范围而不是下标空间。

```python
def findDuplicate(self, nums):
    low = 1
    high = len(nums)-1
   	
    while low < high:
        mid = low+(high-low)/2
        count = 0
        for i in nums:
            if i <= mid:
                count+=1
        if count <= mid:
            low = mid+1
        else:
            high = mid
    return low
```

6/27 [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/description/)<br>
题意：山峰元素都定义是，比相邻的元素都大。现在给定一个数组，可能存在多个山峰元素。找到一个并返回。<br>
典型二分。但思路稍微要转换下。
```
public int findPeakElement(int[] nums) {
    int l = 0, r = nums.length - 1; // left, right
    while (l < r) {
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            r = mid;
        else
            l = mid + 1;
    }
    return l;
}
```
每次取中位数假定为山峰，然后**判断mid和mid+1的大小**.之所以**不用判断i和i-1**，是因为在上一个i(i')的判断过程中，已经判断了i'和i'+1。只有当i'+1元素大于i'时，才能走到下一步i,因此只需往前+1判断。

6/18 [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/description/)<br>
题意：判断一个数是否是完全平方。<br>
把low high mid都改成long再试试看。通过了。<br>
以及，试试low high 只对一个加减1看看。事实证明，只能对low加1。
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

6/17 [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)<br>
题意：一个升序的数组，左边部分元素整体平移了。12345变成45123.搜索指定元素返回下标，否则返回-1.<br>

二分法。但是总是忽略一些边界情况！！！
不知道答案是怎么做的。
```
public int search(int[] nums, int target) {
    int len = nums.length;
    if(len==0) return -1;
    int low = 0, high = len-1, mid;
    while(low<high){
        mid = low + (high - low)/2;
        if(nums[mid] > nums[low]){
            if(nums[low] <= target && target <= nums[mid]) {high = mid; }
            else low = mid+1;
        }
        else {
            if(nums[mid] < target && target <= nums[high]) {low = mid+1; }
            else high = mid;
        }
    }
    if(low==len-1) return nums[low]==target ? low : -1;
    else{
        if(nums[low]==target) return low;
        else if(nums[low+1]==target) return low+1;
        else return -1;
    }
}
```
1空数组没判断！2末尾要判断是否是low还是low+1！！<br>

6/17 [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)<br>
题意：寻找平移过的数组中的最小元素.<br>
做题时候，先看看是否有空数组或者长度为1的特殊情况需要单独判断啊！！！<br>
以下是我的做法：
```
public int findMin(int[] nums) {
    int low = 0, high = nums.length-1, mid;
    if(low==high) return nums[low];
    while(low<high){
        mid = low + (high - low)/2;
        if(nums[mid] > nums[low]){
            if(nums[mid] < nums[high]) high = mid;
            else low = mid+1;
        }
        else{
            high = mid;
        }
    }
    if(low==nums.length-1) return nums[low];
    else return Math.min(nums[low], nums[low+1]);
}
```
以下是最高票答案的做法：<br>
当num[low]比num[high]小的时候，直接返回low，因为在一定区间内，相对大小不改变。厉害啊。
```
public int findMin(int[] nums) {
    int low = 0, high = nums.length-1, mid;
    if(low==high) return nums[low];
    while(low<high){
		//brilliant code!!
        if(nums[low] < nums[high]) return nums[low];
        mid = low + (high - low)/2;
        if(nums[mid] >= nums[low]){
            low = mid+1;
        }
        else{
            high = mid;
        }
    }
    return nums[low];
}
```

6/16 [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)<br>
题意：一个二维矩阵，每一行从左到右升序，每一列从上到下升序。在这个矩阵中寻找指定元素，返回下标，否则返回-1.<br>
其实是答案的思路，但真的很棒。日后看看能否想起来？
```
public boolean searchMatrix(int[][] matrix, int target) {
    if(matrix == null || matrix.length < 1 || matrix[0].length <1) {
        return false;
    }
    int r = matrix.length;
    int c = matrix[0].length;
    int i=0, j=c-1;
    boolean find=false;
    while(i<r&&j>=0){
        if(matrix[i][j]==target) {find=true; break; }
        else if(matrix[i][j]<target) ++i;
        else if(matrix[i][j]>target) --j;
    }
    return find;
}
```
从右上方开始搜索，然后根据目标值往左往右移动搜索。

[74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)<br>
题意：一个矩阵，每行从左到右升序，上一行最右的元素总小于下一行最左元素。搜索target值的元素，否则返回-1.<br>
简单题。然鹅。。
答案怎么做？
```
public boolean searchMatrix(int[][] matrix, int target) {
    int r = matrix.length;
    int c = (r==0 ? 0:matrix[0].length);
    if(r==0||c==0) return false;
    int p=0, q=0;
    while(q<r && matrix[q][c-1]<target) ++q; // q is the row that 'target' exists.
    if(q==r) --q; //if last row, should minus one. 
    int index = Arrays.binarySearch(matrix[q], target);
    return index<0 ? false : true;
}
```
```
bool searchMatrix(vector<vector<int> > &matrix, int target) {
    int n = matrix.size();
    int m = matrix[0].size();
    int l = 0, r = m * n - 1;
    while (l != r){
        int mid = (l + r - 1) >> 1;
        if (matrix[mid / m][mid % m] < target)
            l = mid + 1;
        else 
            r = mid;
    }
    return matrix[r / m][r % m] == target;
}
```
为什么总是不考虑边界情况啊。。。当到边界时候，真的要验证一遍自己的代码有没有错误啊。

6/16 [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)<br>
在一个BST中寻找第k大的元素。 还没想过看follow up如何解决。
以下是二分dfs的方法。其实没看出和二分有啥关系。。就是一个dfs的做法啊。
```
public int kthSmallest(TreeNode root, int k) {
    int count = countNodes(root.left);
    if (k <= count) {
        return kthSmallest(root.left, k);
    }
    else if (k > count + 1) {
        return kthSmallest(root.right, k-1-count); // 1 is counted as current node
    }
    return root.val;
}
public int countNodes(TreeNode n) {
    if (n == null) return 0;   
    return 1 + countNodes(n.left) + countNodes(n.right);
}
```
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?<br>

详细解答看[here](https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63660/3-ways-implemented-in-JAVA-(Python):-Binary-Search-in-order-iterative-and-recursive)<br>

intersection of two arrays 2 
follow up:<br>
What if the given array is already sorted? How would you optimize your algorithm?<br>
What if nums1's size is small compared to nums2's size? Which algorithm is better?<br>
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?<br>

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
