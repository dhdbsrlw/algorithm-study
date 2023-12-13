#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int n, m;

int main() {

    cin >> n >> m; // n 과 m 을 순차적으로 입력받는다.
    map<string, int> man; // 마치 딕셔너리
    vector<string> ans; // 마치 (동적) 배열

    for (int i = 0; i < n + m; i++) {
        string name;
        cin >> name; // name 에 입력값 저장
        man[name]++;
    }

    for (auto iter: man) {
        if (iter.second == 2)
            ans.push_back(iter.first); // 배열의 뒤로 push
    }

    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++) 
        cout << ans[i] << endl;
}