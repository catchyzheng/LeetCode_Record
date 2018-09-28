[200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)



[733. Flood Fill](https://leetcode.com/problems/flood-fill/submissions/1)<br>
改变其中某个元素的值，floodfill到矩阵中相连的和原值相同的所有元素。<br>
主要是两种做法。如果先判断了新颜色和原颜色是不一样后再dfs，则可以不用visited数组记录遍历情况。如果没有判断，就要if(r-1>=0 && !visited[r-1][c])，否则会死循环。<br>
原因在于，颜色不一样的话，已经变成新颜色的地方就相当于是被标记了访问过了。

```
class Solution {
    public boolean[][] visited;
    public int[][] photo;
    public int oldColor;
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        visited = new boolean[image.length][image[0].length];
        photo = image;
        oldColor = image[sr][sc];
        if(oldColor!=newColor) dfs(sr, sc, newColor);
        return photo;
    }
    public void dfs(int r, int c, int newColor){
        if(photo[r][c]==oldColor){
            photo[r][c]=newColor; visited[r][c]=true;
            if(r-1>=0) dfs(r-1, c, newColor);
            if(c-1>=0) dfs(r, c-1, newColor);
            if(r+1<photo.length) dfs(r+1, c, newColor);
            if(c+1<photo[0].length) dfs(r, c+1, newColor);
            return;
        }
        else return;
    }
}

```