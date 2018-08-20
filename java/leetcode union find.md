8/13 [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/solution/)

（本题不是自己做的）题意：给出构成一个图的一组边，找到the last edge，使得当去掉这条边后，剩下的图是一棵树。

方法1：dfs。依次读取边，读过的边组成图。每当读取新的边(u, v)时，就在已知的图中dfs，看能否找到从u到v的通路。如果能行，就返回此边作为结果。（solution解答）

```python
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])#只要有true，就返回true

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
```

方法2：并查集。



8/12 [547. Friend Circles](https://leetcode.com/problems/friend-circles/description/)

题意：一群朋友0-n，有些是直接朋友，有些是间接朋友。现在定义朋友圈为，圈中所有人互相都是直接或者间接朋友，问这群朋友中有多少个“朋友圈”。

实际上就是找多少块联通分量。

方法1：dfs。

```python
class Solution(object):
    cnt = 0
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        vis = [False] * len(M)
        for i in range(len(M)):
            if not vis[i]:
                self.cnt += 1
                vis[i] = True
                self.dfs(M, i, vis)
                
        return self.cnt
        
    def dfs(self, M, i, vis):
        for j in range(len(M)):
            if M[i][j] == 1 and not vis[j]:
                vis[j] = True
                self.dfs(M, j, vis)
```

方法2：disjoint set union。真是剽悍的java并查集模板。。。

```java
public class Solution {
    class UnionFind {
        private int count = 0;
        private int[] parent, rank;
        
        public UnionFind(int n) {
            count = n;
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }
        
        public int find(int p) {
        	while (p != parent[p]) {
                parent[p] = parent[parent[p]];    // path compression by halving
                p = parent[p];
            }
            return p;
        }
        
        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) return;
            if (rank[rootQ] > rank[rootP]) {
                parent[rootP] = rootQ;
            }
            else {
                parent[rootQ] = rootP;
                if (rank[rootP] == rank[rootQ]) {
                    rank[rootP]++;
                }
            }
            count--;
        }
        
        public int count() {
            return count;
        }
    }
    
    public int findCircleNum(int[][] M) {
        int n = M.length;
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (M[i][j] == 1) uf.union(i, j);
            }
        }
        return uf.count();
    }
}
```