#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

vector<int> graph[100];
int visited[100];
// vector<vector<int>> linked; 
// linked(visited) 는 2차원 배열이 아닌 1차원 배열로 생성

void dfs(int x) {
	for (auto i : graph[x]) {
		if (!visited[i]) {
			visited[i] = 1;
			dfs(i);
		}
	}
}

int main(void) {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int v;
			cin >> v;
			if (v)
				graph[i].push_back(j); // 연결되어 있는 노드 번호 삽입
		}
	}

	for (int i = 0; i < n; i++) {
		memset(visited, 0, sizeof(visited)); // 0으로 배열 초기화
		dfs(i);
		// 결과값 출력
		for (int j = 0; j < n; j++)
			cout << visited[j] << " "; // 한 행씩 dfs 수행
		cout << "\n";
	}
}

/*
void dfs(int x) {
	for (auto i : graph[x]) { // 마치 파이썬의 for 문 w/ iterable structure
		if (i == 0)
			continue;
		else {
			linked[x][i] = 1; 
			dfs(i);
		}
	}
}

int main(void) {

	int n; 
	cin >> n;

	// 인접 행렬 값 삽입
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++ ) {
			int v;
			cin >> v;
			graph[i][j] = v;
		}
	}

	// 연결 확인 및 출력
	for (int i = 0; i < n; i++)
		dfs(i);

	return 0;
}
*/