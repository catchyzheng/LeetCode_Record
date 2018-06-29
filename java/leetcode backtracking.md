6/29 [216. Combination Sum III]()

5/27 [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)<br>
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

5/27 [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)<br>
给定总的小括号数，问能生成多少个合法的括号串。典型回溯<br>
n=3,["((()))","(()())","(())()","()(())","()()()"]<br>
令left right为左右括号剩余数。每增加一个括号，就相应地减掉1.但要注意一个点，能减到多少？
```
private List<String> ans = new ArrayList<>();
public List<String> generateParenthesis(int n) {
    int left=n, right=n;
    String s="";
    dfs(s, left, right);
    return ans;
}
void dfs(String s, int l, int r){
    if(l==0&&r==0){
        ans.add(s); return;
    }
    if(l>0) dfs(s+'(', l-1, r); 
    if(r>0&&l<r) dfs(s+')', l, r-1);
    return;
}
```
减到0为止。



