#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> adj;

vector<int> bfs(int start)
{
	vector<bool> discovered(adj.size(), false);
	queue<int> q;
	vector<int> order;
	discovered[start] = true;
	q.push(start);
	while (!q.empty()) {
		int here = q.front();
		q.pop();
		order.push_back(here);
		for (int i = 0; i < adj[here].size(); i++) {
			int there = adj[here][i];
			if (!discovered[there]) {
				q.push(there);
				discovered[there] = true;
			}
		}
	}
	return order;
}

int main()
{
	adj.resize(4);
	adj[0] = { 1, 2 };
	adj[1] = { 2 };
	adj[2] = { 0, 3 };
	adj[3] = { 3 };

	vector<int> path = bfs(2);

	for (int i = 0; i < 4; i++) {
		cout << path[i] << ' ';
	}
	cout << endl;

	return 0;
}