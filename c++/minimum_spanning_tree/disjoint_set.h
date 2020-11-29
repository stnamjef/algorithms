#pragma once
#include <iostream>
#include <vector>
using namespace std;

class DisjointSet
{
private:
	vector<int> parent;
	vector<int> rank;
public:
	DisjointSet(int n);
	int find(int u) const;
	void merge(int u, int v);
};

DisjointSet::DisjointSet(int n):
	parent(n), rank(n, 1)
{
	for (int i = 0; i < n; i++) {
		parent[i] = i;
	}
}

int DisjointSet::find(int u) const
{
	if (u == parent[u]) {
		return u;
	}
	return find(parent[u]);
}

void swap(int& a, int& b)
{
	int temp = a;
	a = b;
	b = temp;
}

void DisjointSet::merge(int u, int v)
{
	u = find(u), v = find(v);
	if (u == v) {
		return;
	}
	if (rank[u] > rank[v]) {
		swap(u, v);
	}
	parent[u] = v;
	if (rank[u] == rank[v]) {
		rank[v]++;
	}
}