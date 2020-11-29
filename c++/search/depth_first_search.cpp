//#include <iostream>
//#include <vector>
//using namespace std;
//
//vector<vector<int>> adj;
//vector<bool> visited;
//
//void dfs(int here)
//{
//	cout << "DFS visits " << here << endl;
//	visited[here] = true;
//	for (int there = 0; there < adj[here].size(); there++) {
//		if (!visited[there] && adj[here][there]) {
//			dfs(there);
//		}
//	}
//}
//
//void dfsAll()
//{
//	visited = vector<bool>(adj.size(), false);
//	for (int i = 0; i < adj.size(); i++) {
//		if (!visited[i]) {
//			dfs(i);
//		}
//	}
//}
//
//int main()
//{
//	adj = {
//		{0, 1, 0, 0, 1},
//		{0, 0, 0, 0, 0},
//		{1, 0, 0, 1, 0},
//		{0, 0, 1, 0, 1},
//		{1, 0, 0, 0, 0}
//	};
//
//	dfsAll();
//
//	return 0;
//}

//void dfs(int here)
//{
//	cout << "DFS visits " << here << endl;
//	visited[here] = true;
//	for (int i = 0; i < adj[here].size(); i++) {
//		int there = adj[here][i];
//		if (!visited[there]) {
//			dfs(there);
//		}
//	}
//}
//
//void dfsAll()
//{
//	visited = vector<bool>(adj.size(), false);
//	for (int i = 0; i < adj.size(); i++) {
//		if (!visited[i]) {
//			dfs(i);
//		}
//	}
//}
//
//int main()
//{
//	adj.resize(5);
//	adj[0] = { 1, 4 };
//	adj[2] = { 0, 3 };
//	adj[3] = { 2, 4 };
//	adj[4] = { 0 };
//
//	dfsAll();
//
//
//	return 0;
//}