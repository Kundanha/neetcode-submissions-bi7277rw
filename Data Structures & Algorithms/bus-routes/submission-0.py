class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = defaultdict(list)

        for route in range(len(routes)):
            for stop in routes[route]:
                adj[stop].append(route)
        

        q = deque()
        visited = set()

        for route in adj[source]:
            q.append(route)
            visited.add(route)
        
        busCount = 1

        while q:
            for _ in range(len(q)):
                route = q.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return busCount
                    for nextRoute in adj[stop]:
                        if nextRoute not in visited:
                            q.append(nextRoute)
                            visited.add(nextRoute)
            busCount+=1
        return -1