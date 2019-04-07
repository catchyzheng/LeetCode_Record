[200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)



[733. Flood Fill](https://leetcode.com/problems/flood-fill/submissions/1)<br>
改变其中某个元素的值，floodfill到矩阵中相连的和原值相同的所有元素。<br>
主要是两种做法。如果先判断了新颜色和原颜色是不一样后再dfs，则可以不用visited数组记录遍历情况。如果没有判断，就要if(r-1>=0 && !visited[r-1][c])，否则会死循环。<br>
原因在于，颜色不一样的话，已经变成新颜色的地方就相当于是被标记了访问过了。

```python
class Solution:
    def floodFill(self, image, sr, sc, newcolor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldcolor = image[sr][sc]
        self.dfs(image, sr, sc, newcolor, oldcolor)
        return image
        
        
    def dfs(self, image, sr, sc, color, oldcolor):
        image[sr][sc] = color
        dirt = [[1,0], [-1,0], [0,1], [0,-1]]
        for di in dirt:
            x = sr + di[0]; y = sc + di[1]
            if x>=0 and x<len(image) and y>=0 and y<len(image[0]) and image[x][y] != color and image[x][y] == oldcolor:
                self.dfs(image, x, y, color, oldcolor)
        
```