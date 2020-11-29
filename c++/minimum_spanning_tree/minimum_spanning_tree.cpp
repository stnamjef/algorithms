#include <utility>
#include <algorithm>
#include "disjoint_set.h"
using namespace std;

int INF = 1000000000;

// (adjacent vertex, weight)
vector<vector<pair<int, int>>> adj;

int kruskal(vector<pair<int, int>>& selected)
{
	int ret = 0;
	selected.clear();
	// (weight, (vertex1, vertex2))
	vector<pair<int, pair<int, int>>> edges;
	for (int u = 0; u < adj.size(); u++) {
		for (int i = 0; i < adj[u].size(); i++) {
			int v = adj[u][i].first, cost = adj[u][i].second;
			edges.push_back(make_pair(cost, make_pair(u, v)));
		}
	}
	// sort by weight, ascending order
	stable_sort(edges.begin(), edges.end());
	DisjointSet sets(adj.size());
	for (int i = 0; i < edges.size(); i++) {
		int cost = edges[i].first;
		int u = edges[i].second.first, v = edges[i].second.second;
		if (sets.find(u) == sets.find(v)) {
			continue;
		}
		sets.merge(u, v);
		selected.push_back(make_pair(u, v));
		ret += cost;
	}
	return ret;
}

int prim(vector<pair<int, int>>& selected)
{
	int V = adj.size();
	selected.clear();
	vector<bool> added(V, false);
	vector<int> min_weight(V, INF), parent(V, -1);

	int ret = 0;
	min_weight[0] = parent[0] = 0;
	for (int iter = 0; iter < V; iter++) {
		int u = -1;
		for (int v = 0; v < V; v++) {
			if (!added[v] && (u == -1 || min_weight[u] > min_weight[v])) 
				u = v;
		}
		if (parent[u] != u)
			selected.push_back(make_pair(parent[u], u));
		ret += min_weight[u];
		added[u] = true;
		for (int i = 0; i < adj[u].size(); i++) {
			int v = adj[u][i].first, weight = adj[u][i].second;
			if (!added[v] && min_weight[v] > weight) {
				parent[v] = u;
				min_weight[v] = weight;
			}
		}
	}
	return ret;
}

int main()
{
	adj = {
		{{1, 1}, {2, 3}},
		{{0, 1}, {2, 3}, {3, 6}},
		{{0, 3}, {1, 3}, {3, 4}, {4, 2}},
		{{1, 6}, {2, 4}, {4, 5}},
		{{2, 2}, {3, 5}}
	};

	cout << "adjacent list:" << endl;
	for (int i = 0; i < 5; i++) {
		cout << "from: " << i << " ---> ";
		for (int j = 0; j < adj[i].size(); j++) {
			cout << "(to: " << adj[i][j].first;
			cout << ", w: " << adj[i][j].second << "), ";
		}
		cout << endl;
	}
	cout << endl;

	vector<pair<int, int>> selected;
	int cost = kruskal(selected);

	cout << "Kruskal algorithm --> cost:" << cost << ", ";
	cout << "edges:";
	for (int i = 0; i < selected.size(); i++) {
		cout << '(' << selected[i].first << ' ';
		cout << selected[i].second << ") ";
	}
	cout << endl;

	cost = prim(selected);

	cout << "Prim algorithm    --> cost:" << cost << ", ";
	cout << "edges:";
	for (int i = 0; i < selected.size(); i++) {
		cout << '(' << selected[i].first << ' ';
		cout << selected[i].second << ") ";
	}
	cout << endl;

	return 0;
}