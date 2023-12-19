#include <iostream>
using namespace std;

// 고민되는 지점: 미리 모두 구해놓기 vs. 필요할 때 필요한만큼 구하기

int getNum(int k, int n) {
	if (n == 1) // 1호일 경우
		return 1;
	if (k == 0)
		return n;
	// 재귀로 구현
	return (getNum(k - 1, n) + getNum(k, n - 1));
}

int main(void) {

	int t;
	cin >> t;
	
	/*
	vector<vector<int>> apt;
	for (int i = 1; i < 15; i++) {
		apt[0].push_back(i);
	}
	*/

	for (int i = 0; i < t; i++) {
		
		int num = 0;
		int k, n;
		cin >> k >> n;
		cout << getNum(k, n) << '\n';
	}

	return 0;
}