```python
class Solution:
    def findShortestWay(self, maze_, ball, hole):
        # 1 is wall, 0 is plain, -1 is treasure
        maze = [[ 0, 0,-1, 0, 0],\
                [ 1, 1, 0, 0, -1],\
                [ 0, 1,-1, 0, -1],\
                [-1, 1, 0, 0, 0],\
                [-1, 1,-1, 0, 0]]
        
        m = len(maze); n = len(maze[0])
        visit = [[0 for _ in range(n)] for __ in range(m)]
        start = [0, 0]
        end = [m-1, n-1]
        self.cnt = 0
        treasure = []
        # find all treasure location
        #just use dfs and visit array to record treasure number and visited cell. 
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
        
        
        #use dfs to find the shortest path visiting all treasures
        #backtracking. 
        #record the steps and treasure counts during dfs.
        #the conditions are 1 reach the end point and 2 visit all treasures
        #basic idea is to search each path using DFS and find the best.
        visit = [[0 for _ in range(n)] for __ in range(m)]
        self.min_steps = float('inf')
        def dfs2(maze, sx, sy, count, steps):
            if sx==end[0] and sy==end[1] and count==self.cnt:
                self.min_steps = min(steps, self.min_steps)
                return
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            for d in dirs:
                x = sx + d[0]; y = sy + d[1]
                if x>=0 and x<m and y>=0 and y<n and visit[x][y]==0 and maze[x][y]!=1:
                    visit[x][y]=1
                    if maze[x][y]==-1:
                        dfs2(maze, x, y, count+1, steps+1)
                    else:
                        dfs2(maze, x, y, count, steps+1)
                    visit[x][y]=0
                    
        dfs2(maze, start[0], start[1], 0, 1)
        print(self.min_steps)
        
        # use bfs to find shortest path visiting all treasures.
        #set total step as 0. set start point as '2'.
        #start from start point, and BFS through the maze, record step and mark visited cell as '1' during BFS
        #if reach a treasure, add step onto total step. set this cell as '2', and change all visited '1' into 0. 
        #start new round BFS from this treasure. 
        #and reach another treasure. continue the loop. 
        #finally would reach to all treasures. (tested true)
        #but, the total step count is a little weird...... unsolved yet.
        trea = 0
        visit = [[0 for _ in range(n)] for __ in range(m)]
        visit[start[0]][start[1]] = 2 # 2 to mark it as un changeable point
        qu = [start]
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        
        new_start = []
        step_cnt = 0
        step_sum = 1
        tmp_qu = []
        while len(qu) > 0 and trea < self.cnt:
            top = qu.pop()
            for d in dirs:
                x = top[0] + d[0]; y = top[1] + d[1]
                if x>=0 and x<m and y>=0 and y<n and visit[x][y]==0 and maze[x][y]!=1:
                    if maze[x][y]==0:
                        visit[x][y] = 1
                        tmp_qu.append([x,y])
                    elif maze[x][y] == -1 or (x==end[0] and y==end[1]):
                        trea += 1
                        for i in range(m):
                            for j in range(n):
                                if visit[i][j]==1: visit[i][j] = 0
                        visit[x][y] = 2
                        step_sum += step_cnt + 1
                        print('find treasure!', step_cnt+1, step_sum, x, y)
                        step_cnt = 0
                        qu = [[x, y]]
                        break
            if len(qu) == 0:
                qu = copy.copy(tmp_qu)
                tmp_qu = []
                step_cnt += 1
        
        print(step_sum)
        
        #在两个点之间寻找最短路径。BFS.
        '''
        dest = [0, 4]
        tmp_qu = []
        isfind = False
        step = 0
        while len(qu) > 0:
            top = qu.pop()
            for d in dirs:
                x = d[0] + top[0]; y = d[1] + top[1]
                if x>=0 and x<m and y>=0 and y<n and visit[x][y]==0 and maze[x][y]!=1:
                    if not (x == dest[0] and y ==dest[1]):
                        visit[x][y] = 1
                        tmp_qu.append([x,y])
                    else:
                        isfind = True
                        step += 1
                        break
                        
            if isfind:
                break
            if len(qu)==0:
                qu = copy.copy(tmp_qu)
                tmp_qu = []
                step += 1
        
        print('steps: ', step)'''
        
        
        return
```

