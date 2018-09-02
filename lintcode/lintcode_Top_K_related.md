很久以前做的topk题目，现在已经基本都快速想到思路了。

[471. Top K Frequent Words](http://www.lintcode.com/en/problem/top-k-frequent-words/)<br>
找到一堆单词中出现次数前k多的单词，次数相同就按照字典序排。
map存单词和次数。set用于排序，重写了比较函数。
貌似没法边统计次数边排序？。。。耗时末16%。。。

```
struct MyComp{
    bool operator()(const pair<string, int> &a, const pair<string, int> &b){
        if(a.second!=b.second) return a.second>b.second;
        return a.first<b.first;
    }
};
class Solution {
public:
    vector<string> topKFrequentWords(vector<string> &words, int k) {
        map<string, int> Map;
        for(int i=0; i<words.size(); i++) Map[words[i]]++;
        set<pair<string, int>, MyComp> Set;
        map<string, int>::iterator it=Map.begin();
        for(; it!=Map.end(); ++it){
            Set.insert(make_pair(it->first, it->second));
        }
        set<pair<string, int>, MyComp>::iterator set_it=Set.begin();
        int cnt=0;
        vector<string> ans;
        while(cnt<k){
            ans.push_back((*set_it).first);
            ++cnt; ++set_it;
        }
        return ans;
    }
};
```

[545. Top k Largest Numbers II](http://www.lintcode.com/en/problem/top-k-largest-numbers-ii/)<br>
也没啥，就是实现一个优先队列，add操作和获取前k个操作。
就是**优先队列的元素pop完后要再push回去咯**。
```
class Solution {
public:
    priority_queue<int > pq;
    int K;
    Solution(int k) {
        priority_queue<int > pq; this->pq = pq; K=k;
    }
    void add(int num) {pq.push(num); }
    vector<int> topk() {
        vector<int> ans;
        queue<int> qu;
        for(int i=0; i<K; i++){
            if(pq.empty()) break;
            ans.push_back(pq.top()); qu.push(pq.top()); pq.pop(); 
        }
        while(!qu.empty()){
            pq.push(qu.front()); qu.pop();
        }
        return ans;
    }
};
```
[612. K Closest Points](http://www.lintcode.com/en/problem/k-closest-points/#)<br>
题意：给定一系列点和一个点a，找出距离点a距离最近的k个点。要求当距离相同时按照x坐标排序，再按照y坐标排序。<br>
这题做得愁死我了。。。。以下是几个关键点：<br>
1如何存放点和距离。我用set<pair<int, Point>, Comp>存放。<br>
2如何比较优先次序。我重载了set比较器Comp，具体如下代码。<br>
此题，数据结构的设计是关键。耗时末59%
```
struct Comp{
	bool operator()(const pair<int, Point> &a, const pair<int, Point> &b){
		if(a.first != b.first) return a.first < b.first;
		else {
			if(a.second.x!=b.second.x) return a.second.x<b.second.x;
			else return a.second.y <= b.second.y;
		}
	}
};
class Solution {
public:
    vector<Point> kClosest(vector<Point> &points, Point &origin, int k) {
        set<pair<int, Point>, Comp > dist;
        for(int i=0; i<points.size(); i++){
        	int distance = (points[i].x-origin.x)*(points[i].x-origin.x) + (points[i].y-origin.y)*(points[i].y-origin.y);
        	dist.insert(make_pair(distance, points[i]));
        }
        vector<Point> ans; 
        set<pair<int, Point> >::iterator it=dist.begin();
        int cnt=0;
        for(; it!=dist.end(); ++it){
			ans.push_back( (*it).second );
			cnt++;
			if(cnt==k) break;
        }
        return ans;
    }
};
```