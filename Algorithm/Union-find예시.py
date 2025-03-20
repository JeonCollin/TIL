# 1. make-set
# 0번 ~ 10번까지
# 처음에는 자신이 부모
parents = [i for i in range(11)]

# 2. find: 최상위 부모 찾기
def find(a):
    
    # 자신의 부모가 자신이면 리턴
    if(parents[a] == a):
        return a
    
    # 자신의 부모의 부모를 찾는다
    return find(parents[a])

# 2-1. 경로 압축
def find_comp(a):
    
    # 자신의 부모가 자신이면 리턴
    if(parents[a] == a):
        return a
    
    # 부모의 부모를 부모로 삼는다
    parents[a] = find_comp(parents[a])
    return parents[a]

# 3. union: 서로소 트리를 합친다
def union(a, b):
    # a와 b의 부모를 찾는다
    ap = find(a)
    bp = find(b)
    
    # a > b 포함시킨다
    parents[bp] = ap
    
# 3-1. rank: 항상 작은 트리를 큰 트리에 붙임
# 처음 rank는 모두 1
rank = [1 for _ in range(11)]
def union(a, b):
    
    ap = find(a)
    bp = find(b)
    
    # 랭크가 더 큰 쪽으로 종속시킨다
    if(rank[ap] <= rank[bp]):
        parents[ap] = bp
        
        # 1. 연결된 노드 수(size) 기준
        rank[bp] += rank[ap]
    
        # 2. 트리 높이 기준
        if(rank[ap] == rank[bp]):
            rank[bp] += 1
            
    else:
        parents[bp] = ap
        
        rank[ap] += rank[bp]