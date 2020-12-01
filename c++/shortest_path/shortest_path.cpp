#include <iostream>
#include <vector>
#include <utility>
#include <queue>
using namespace std;

int INF = 1000000000;
int V = 5;

vector<vector<pair<int, int>>> adj;

vector<int> dijkstra(int start)
{
	vector<int> dist(V, INF);
	dist[start] = 0;
	priority_queue<pair<int, int>> pq;
	pq.push(make_pair(0, start));
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int here = pq.top().second;
		pq.pop();
		if (dist[here] < cost) continue;
		for (int i = 0; i < adj[here].size(); i++) {
			int there = adj[here][i].first;
			int next_dist = cost + adj[here][i].second;
			if (dist[there] > next_dist) {
				dist[there] = next_dist;
				pq.push(make_pair(-next_dist, there));
			}
		}
	}
	return dist;
}

int main()
{
	adj.resize(V);
	adj[0] = { {1, 7}, {2, 4}, {3, 6}, {4, 1} };
	adj[2] = { {1, 2}, {3, 5} };
	adj[3] = { {1, 3} };
	adj[4] = { {3, 1} };

	vector<int> dist = dijkstra(0);
	for (int i = 0; i < dist.size(); i++) {
		cout << dist[i] << ' ';
	}

	return 0;
}