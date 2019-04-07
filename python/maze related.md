10.28 [499. The Maze III](https://leetcode.com/problems/the-maze-iii/description/)

given a maze, 0 is ground, 1 is wall, -1 is treasure. You need to find how many treasure can be reached.

0是平地1是墙-1宝藏。就是从一个0开始，dfs找所有可达-1.

```python
class Solution(object):
    def hasPath(self):
    	maze = [[ 0, 0,-1, 0, 0],\
                [ 1, 1, 0, 0, 1],\
                [ 0, 1,-1, 0,-1],\
                [-1, 1, 0, 0, 1],\
                [-1, 1,-1, 0, 0]]
        
        m = len(maze); n = len(maze[0])
        visit = [[0 for _ in range(n)] for __ in range(m)]
        start = [0, 0]
        self.cnt = 0
        treasure = []
        def dfs(maze, sx, sy):
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            
            for d in dirs:
                x = sx+d[0]; y = sy + d[1]
                if x>=0 and x<m and y>=0 and y<n and maze[x][y]!=1 and visit[x][y]==0:
                    visit[x][y] = 1
                    if maze[x][y]==-1: 
                        self.cnt += 1
                        treasure.append([x, y])
                    dfs(maze, x, y)
        visit[start[0]][start[1]] = 1
        dfs(maze, start[0], start[1])
        
        print(self.cnt)
```



10.27 [505. The Maze II](https://leetcode.com/problems/the-maze-ii/description/)



给定一个矩阵，0表示空地1表示墙。给定球的位置和洞口位置，都在空地上。球会沿着一个方向一直滚直到遇到墙或者边界。问**最短路径是多少，并输出**。maze3是问依次输出球滚动的方向。大不了每次计算两个相邻路径点之间的相对位置，然后返回方向。

还没看dijstra算法怎么做的。。。。

```python
class Solution(object):
    def shortestDistance(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        dist = [[float('inf') for _ in range(n)] for __ in range(m)]
        dist[start[0]][start[1]] = 0
        pre = [[ [-1, -1] for _ in range(n)] for __ in range(m)]
        action = [[ '0' for _ in range(n)] for __ in range(m)]
        
        self.dfs(maze, start, dist, pre, action)
        
        for i in range(m):
            for j in range(n):
                print dist[i][j],
            print ''
        if dist[dest[0]][dest[1]] == float('inf'):
            return -1
        else: 
            xx, yy = dest[0], dest[1]
            print [xx, yy]
            while [xx, yy] != start:
                # print the path
                print pre[xx][yy]
                [xx, yy] = pre[xx][yy]
                # should not xx = pre[xx][yy][0]; yy = pre[xx][yy][1] !!!
            return dist[dest[0]][dest[1]]
        
    def dfs(self, maze, start, dist, pre, action):
        dirs = [[-1,0], [1,0], [0, -1], [0,1]]
        #hmap = ['u', 'd', 'r', 'l']
        #i = 0
        for d in dirs:
            #i += 1
            x = start[0] + d[0]
            y = start[1] + d[1]
            cnt = 0
            #while表示会一直向一个方向走直到遇到阻碍，中间过程不记录。
            #if表示一次移动一步。
            while x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]!=1:
                x += d[0]; y += d[1]
                cnt += 1
            if dist[x-d[0]][y-d[1]] > dist[start[0]][start[1]] + cnt:
                dist[x-d[0]][y-d[1]] = dist[start[0]][start[1]] + cnt
                pre[x-d[0]][y-d[1]] = [start[0], start[1]]
                #action[x-d[0]][y-d[1]] = hmap[i%4]
                #print pre[x-d[0]][y-d[1]]
                self.dfs(maze, [x-d[0], y-d[1]], dist, pre, action)
        
```

[Dijstra](https://leetcode.com/problems/the-maze-ii/solution/)

```java
public class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] dest) {
        int[][] distance = new int[maze.length][maze[0].length];
        for (int[] row: distance)
            Arrays.fill(row, Integer.MAX_VALUE);
        distance[start[0]][start[1]] = 0;
        dijkstra(maze, start, distance);
        return distance[dest[0]][dest[1]] == Integer.MAX_VALUE ? -1 : distance[dest[0]][dest[1]];
    }

    public void dijkstra(int[][] maze, int[] start, int[][] distance) {
        int[][] dirs={{0,1},{0,-1},{-1,0},{1,0}};
        PriorityQueue < int[] > queue = new PriorityQueue < > ((a, b) -> a[2] - b[2]);
        queue.offer(new int[]{start[0],start[1],0});
        while (!queue.isEmpty()) {
            int[] s = queue.poll();
            if(distance[s[0]][s[1]] < s[2]) //the old record for distance, should abandon
                continue;
            for (int[] dir: dirs) {
                int x = s[0] + dir[0];
                int y = s[1] + dir[1];
                int count = 0;
                while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                    count++;
                }
                if (distance[s[0]][s[1]] + count < distance[x - dir[0]][y - dir[1]]) {
                    distance[x - dir[0]][y - dir[1]] = distance[s[0]][s[1]] + count;
                    queue.offer(new int[]{x - dir[0], y - dir[1], distance[x - dir[0]][y - dir[1]]});
                }
            }
        }
    }
}
```

