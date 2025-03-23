class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # nodes: [time, number of ways]
        nodes = [[-1, -1] for _ in range(n)]
        adj_list = [[] for _ in range(n)]
        
        # Build the graph
        for u, v, cost in roads:
            adj_list[u].append((cost, v))
            adj_list[v].append((cost, u))
        
        # Priority queue (min-heap)
        min_heap = [(0, 0)]  # (time, node)
        heapq.heapify(min_heap)
        nodes[0] = [0, 1]  # Starting node
        
        while min_heap:
            time, u = heapq.heappop(min_heap)
            
            # If this node's time is not the most recent, it's a stale entry
            if time > nodes[u][0]:
                continue
            
            for cost, v in adj_list[u]:
                total = time + cost
                
                if total == nodes[v][0]:
                    # Found another way to reach v with the same minimum time
                    nodes[v][1] = (nodes[v][1] + nodes[u][1]) % MOD
                elif nodes[v][0] == -1 or total < nodes[v][0]:
                    # Found a shorter path to v
                    nodes[v] = [total, nodes[u][1]]
                    heapq.heappush(min_heap, (total, v))
        
        return nodes[-1][1]  # Return the number of ways to reach node n-1




