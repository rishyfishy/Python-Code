# Modified BFS on an unweighted bipartite graph
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """

        edges=[[edge[0],edge[1]+n] for edge in redEdges]
        edges+=([[edge[0]+n,edge[1]] for edge in blueEdges])
        graphMap={}

        for edge in edges:
            if graphMap.has_key(edge[0]):
                graphMap[edge[0]].append(edge[1])
            else:
                graphMap[edge[0]]=[edge[1]]

        dist = list((2*n)*[2*n+1])
        prev = list((2*n)*[None])

        dist[0],dist[n]=0,0

        Q = [n,0]

        while len(Q):
            u=Q.pop()
            print("u=" + str(u))
            if graphMap.has_key(u):
                for neighboor in graphMap[u]:
                    print(neighboor)
                    if dist[neighboor]>dist[u]+1:
                        dist[neighboor]=dist[u]+1
                        prev[neighboor]=u
                        Q.insert(0,neighboor)

        print(dist)


        ans = [min(dist[i],dist[i+n]) for i in range(n)]

        for i in range(n):
            if ans[i]== 2*n+1:
                ans[i]=-1

        return ans


