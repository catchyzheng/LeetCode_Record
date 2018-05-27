[39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)<br>
给定一个元素互不相同的数组以及一个目标值，要求返回一个list<list<>>，存放着所有不同的组合方式。元素可重复使用。
```
List<List<Integer>> ans = new ArrayList<>();
List<Integer> list = new ArrayList<>();
public List<List<Integer>> combinationSum(int[] c, int t) {
    int len = c.length;
    dfs(c, t, 0);
    return ans;
}
public void dfs(int [] c, int t, int index){
    if(t==0){
        List<Integer> tmp = new ArrayList<>();
        for(int ele: list){
            tmp.add(ele);
        }
        ans.add(tmp); return;
    }
    for(int i=index;i<c.length; ++i){
        if(t-c[i]>=0){
            list.add(c[i]);
            dfs(c, t-c[i], i);
            list.remove(list.size()-1);
        }
    }
    return;
}
```

