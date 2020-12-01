#include <iostream>
#include <utility>
#include <queue>
using namespace std;

struct Node
{
	char symbol;
	double freq;
	Node* left;
	Node* right;
	Node(char symbol, double freq, Node* left = nullptr, Node* right = nullptr) :
		symbol(symbol), freq(freq), left(left), right(right) {}
};

struct cmp
{
	bool operator()(Node* a, Node* b) {
		return (a->freq > b->freq);
	}
};

Node* encode(const vector<pair<char, double>>& freqs)
{
	priority_queue<Node*, vector<Node*>, cmp> pq;

	for (int i = 0; i < freqs.size(); i++) {
		pq.push(new Node(freqs[i].first, freqs[i].second));
	}

	Node* left, * right, * top;
	while (pq.size() > 1) {
		left = pq.top();
		pq.pop();

		right = pq.top();
		pq.pop();

		top = new Node('*', left->freq + right->freq, left, right);
		pq.push(top);
	}

	return pq.top();
}

void print_codes(Node* node, string str)
{
	if (node != nullptr) {
		if (node->symbol != '*') {
			cout << node->symbol << ": " << node->freq << ": " << str << endl;
		}
		print_codes(node->left, str + "0");
		print_codes(node->right, str + "1");
	}
}

void delete_memory(Node* node)
{
	if (node != nullptr) {
		delete_memory(node->left);
		delete_memory(node->right);
		delete node;
	}
}

int main()
{
	vector<pair<char, double>> freqs;
	freqs = {
		{ 'a', 8.167 }, { 'b', 1.492 }, { 'c', 2.782 }, { 'd', 4.253 },
		{ 'e', 12.702 }, { 'f', 2.228 }, { 'g', 2.015 }, { 'h', 6.094 },
		{ 'i', 6.966 }, { 'j', 0.153 }, { 'k', 0.747 }, { 'l', 4.025},
		{ 'm', 2.406 }, { 'n', 6.749 }, { 'o', 7.507 }, { 'p', 1.929 },
		{ 'q', 0.095 }, { 'r', 5.987 }, { 's', 6.327 }, { 't', 9.056 },
		{ 'u', 2.758 }, { 'v', 1.037 }, { 'w', 2.365 }, { 'x', 0.150 },
		{ 'y', 1.974 }, { 'z', 0.074 }
	};

	Node* top = encode(freqs);

	print_codes(top, "");
	delete_memory(top);

	return 0;
}