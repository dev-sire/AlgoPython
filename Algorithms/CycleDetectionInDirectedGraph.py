# Author: Aman Shahid
def is_cyc_util(adj, u, visited, rec_stack):
    if not visited[u]:
        visited[u] = True
        rec_stack[u] = True
        for x in adj[u]:
            if not visited[x] and is_cyc_util(adj, x, visited, rec_stack):
                return True
            elif rec_stack[x]:
                return True
    rec_stack[u] = False
    return False
def is_cyclic(adj, V):
    visited = [False] * V
    rec_stack = [False] * V
    for i in range(V):
        if not visited[i] and is_cyc_util(adj, i, visited, rec_stack):
            return True
    return False
if __name__ == "__main__":
    V = 4
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(3)
    if is_cyclic(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")
