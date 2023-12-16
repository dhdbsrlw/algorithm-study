#include <iostream>
#include <vector>
// #include <utility>
using namespace std;
pair <char, char> node[26]; // 좌, 우 자식 노드

void preorder(char root) {
	if (root == '.') // 없는 노드
		return; // 재귀 종료

	cout << root;
	preorder(node[root - 'A'].first);
	preorder(node[root - 'A'].second);
}

void inorder(char root) {
	if (root == '.') // 없는 노드
		return; // 재귀 종료

	inorder(node[root - 'A'].first);
	cout << root;
	inorder(node[root - 'A'].second);
}

void postorder(char root) {
	if (root == '.') // 없는 노드
		return; // 재귀 종료

	postorder(node[root - 'A'].first);
	postorder(node[root - 'A'].second);
	cout << root;
}

int main(void) {

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		char root, left, right;
		cin >> root >> left >> right;
		node[root - 'A'].first = left; // 대문자를 아스키코드 값을 변환하여 배열의 인덱스로 지정
		node[root - 'A'].second = right;
	}

	// 순회 결과 출력
	preorder('A');
	cout << "\n";
	inorder('A');
	cout << "\n";
	postorder('A');

	return 0;
}