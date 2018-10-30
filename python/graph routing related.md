10.30 [Route Between Two Nodes in Graph](https://www.lintcode.com/problem/route-between-two-nodes-in-graph/discuss)

判断一个有向无环图中从起点到终点是否可达。

自己的dfs超时了。。。。还是学习学习下面这个短小精悍的代码吧。。。。

```python
class Solution:
    def __init__(self):
        self.seen = set()
        
    def hasRoute(self, graph, s, t):
        self.seen.add(s)
        if s == t: return True
        return any(self.hasRoute(graph, v, t) for v in s.neighbors if v not in self.seen)
```

```python
    def hasRoute(self, graph, s, t):
        # write your code here
        l = len(graph)
        hmap = dict()
        cnt = 0
        for node in graph:
            hmap[node] = cnt
            cnt += 1
        
        visit = [False for _ in range(cnt)]
        self.reach = False
        def dfs(graph, start):
            if start == t:
                self.reach = True; return
            for ele in start.neighbors:
                if not visit[hmap[ele]]:
                    visit[hmap[ele]] = True
                    dfs(graph, ele)
                    visit[hmap[ele]] = False
                if self.reach:
                    break
        visit[hmap[s]] = True
        dfs(graph, s)
        return self.reach
```

