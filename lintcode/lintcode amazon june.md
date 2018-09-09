9/8 [1479. 能否到达终点](https://www.lintcode.com/problem/can-reach-the-endpoint/description?_from=ladder&&fromId=62)

很基础的队列式BFS。要掌握！

```python
class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        import Queue
        q = Queue.Queue()
        if map is None:
            return None
        m = len(map)
        n = len(map[0])
        
        dirt = [[0,1],[0,-1],[1,0],[-1,0]]
        input_v = [0,0]
        q.put(input_v)
       
        while not q.empty():
            head = q.get()
           
            for x,y in dirt:
                newx, newy = head[0]+ x, head[1] + y   
                if newx >= 0 and newy >= 0 and newx < m and newy < n and map[newx][newy] == 1: 
                    q.put([newx,newy])
                    map[newx][newy] = 0
                elif newx >= 0 and newy >= 0 and newx < m and newy < n and map[newx][newy] == 9: 
                    return True
                    
                     
        return False
```

