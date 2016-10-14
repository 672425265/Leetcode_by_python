# coding: utf-8

'''
并查集

1. 查询 Find
int find(x){
    int parent = father.get(x);
    while(parent != father.get(parent)) {
        parent = father.get(parent);
    }
    return parent;
}
时间复杂度: O(n)

2. 合并 Union
void union(int x, int y){
    int fa_x = find(x);
    int fa_y = find(y);
    if(fa_x != fa_y)
        father.put(fa_x, fa_y);
}
HashMap<Integer, Integer> father = new HashMap<Integer, Integer>();
时间复杂度: O(n)

题目:
1. 关于集合合并
2. 判断在不在同一个集合中
'''







