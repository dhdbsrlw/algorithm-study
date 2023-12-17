#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 우선순위 큐는 힙으로 구현
// 이 문제의 경우 '최대힙'으로 구현
int main(void) {
	int t_case;
	cin >> t_case;

	// 각 테스트케이스에 대해 문서가 몇번째로 인쇄되는지 출력
	for (int i = 0; i < t_case; i++) {
		int n, m;
		cin >> n >> m;
		
		int seq = 0; // 몇 번째로 인쇄 ?
		queue<pair<int, int>> q;
		priority_queue<int> pq; // 최대힙 디폴트

		for (int j = 0; j < n; j++) {
			int x;
			cin >> x;

			q.push({ j, x }); // {문서의 인덱스, 중요도}
			pq.push(x); // 중요도 높은 순으로 삽입
		}

		while (!q.empty()) {
		
			int idx = q.front().first;
			int pri = q.front().second;
			q.pop();

			if (pq.top() == pri) {
				pq.pop();
				seq++;

				if (idx == m) {
					cout << seq << '\n';
					break;
				}
			}
			else
				q.push({ idx,pri }); // 큐의 뒤쪽에 다시 삽입
		}
	}

	return 0;
}