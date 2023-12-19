
#include <bits/stdc++.h>
using namespace std;

// 트라이 활용

struct Trie {
	Trie* node[26]; // 왜냐하면, 알파벳은 총 26글자

	Trie() {
		for (int i = 0; i < 26; i++)
			node[i] = NULL;
	}

	void insert(string& str, int idx) {
		if (idx == str.size()) return;
		if (node[str[idx] - 'a'] == NULL)
			node[str[idx] - 'a'] = new Trie(); 
		
		node[str[idx] - 'a']->insert(str, idx + 1);
	}

	bool find(string& str, int idx) {
		if (idx == str.size()) return true;
		if (node[str[idx] - 'a'] == NULL) return false;

		return node[str[idx] - 'a']->find(str, idx + 1);
 	}

	void clear(void) { // 마치 destroy
		for (int i = 0; i < 26; i++) {
			if (node[i] != NULL) {
				node[i]->clear();
				delete node[i];
			}
		}
	}
};

int main(void) {

	ios::sync_with_stdio(false); // IO 오퍼레이션을 빠르게 한다. (C와 C++ 스타일 혼용을 금지한다.)
	cin.tie(0);
	cout.tie(0);

	int n, m;
	cin >> n >> m;

	Trie* root = new Trie();

	for (int i = 0; i < n; i++) {
		string str;
		cin >> str;
		root->insert(str, 0);
	}

	int cnt = 0;
	for (int i = 0; i < m; i++) {
		string str;
		cin >> str;

		if (root->find(str, 0)) cnt++;
	}

	cout << cnt << "\n";
	root->clear();
	delete root;
	return 0;
}