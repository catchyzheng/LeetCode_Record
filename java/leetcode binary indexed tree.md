
修改从x开始的树状数组。
```
void add(int x, int v) {
    for(int i = x; i <= n; i += lowbit(i))
        C[i] += v;
}
```
初始化
```
for(int i = 1; i <= n; i++) {
    add(i, A[i]);
}
```
求区间和。sum(i) = sum(i - lowbit(i))+ C[i]。
```
int sum(int x){
    int res = 0;
    for(int i = x; i > 0; i -= lowbit(i)) {
        res += C[i];
    }
    return res;
}
```