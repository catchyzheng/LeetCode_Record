10.8 [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)

可能是迄今为止做过的最简单的一个hard。。但是思路有很多，dp， stack， 双指针。

看了答案后的自己的dp。。。

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l <= 2: return 0
        left = [0] * l 
        right = [0] * l
        for i in range(1, l):
            left[i] = max(left[i-1], height[i-1])
        for j in range(l-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])
        sum = 0
        for i in range(l):
            water = min(left[i], right[i]) - height[i]
            sum += water if water > 0 else 0
        return sum
```

记录每个下标的左边最高点和右边最高点，然后算出当前位置上面能放多少水。

双指针的更精妙，日后可以自己想想如何实现。[solution](https://leetcode.com/problems/trapping-rain-water/solution/)

```c++
int trap(vector<int>& height)
{
    int left = 0, right = height.size() - 1;
    int ans = 0;
    int left_max = 0, right_max = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            height[left] >= left_max ? (left_max = height[left]) : ans += (left_max - height[left]);
            ++left;
        }
        else {
            height[right] >= right_max ? (right_max = height[right]) : ans += (right_max - height[right]);
            --right;
        }
    }
    return ans;
}
```

从两端遍历，每次判断左边大还是右边。然后