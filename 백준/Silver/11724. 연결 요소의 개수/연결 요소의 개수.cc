#include <iostream>
#include <vector>
using namespace std;

int n, m;
bool visited[1001];
vector<int> graph[1001];
int cnt = 0;

void dfs(int x) {
	visited[x] = true;
	for (auto i : graph[x])
		if (!visited[i])
			dfs(i);
}

// 무방향 그래프
int main() {

	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	// 노드 1 부터 시작
	for (int i = 1; i < n + 1; i++) {
		if (visited[i])
			continue;
		else {
			cnt++;
			dfs(i);
		}
	}

	cout << cnt;
}