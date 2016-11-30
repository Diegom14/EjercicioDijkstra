import sys
import queue

def dijkstra(G,s):
	desde = [ 0 for _ in range(len(G))]

	dist = [sys.maxsize for _ in range len(G)]

	dist[s] = 0
	Pq = Queue(dist) #cola de prioridad
	Pq.insert(s,0)

	while(!Pq.Empty):

		V = Pq.PopMin() # saca el menor

		for w in G[v]:
			actualizar(V,w)


def actualizar(V,w):

	if dist[V]> dist[V] + w[V,w]:
		dist[w] = dist[V] + w(V,w)
		desde[w] = V
	if w in Pq:
		Pq.Update(w,dist[w])
	else:
		Pq.insert(w,dist[w])

