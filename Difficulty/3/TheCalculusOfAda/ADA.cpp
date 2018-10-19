#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

pair<int, int> ADA(vector<int> cur) {
	pair<int, int> ans(0, 0); int first, second;
	if (cur.size() > 1) {
		bool same = true; int test = cur[0];
		for (int i = 0; i < cur.size(); i++) {
			if (test != cur[i]) {
				same = false;
				break;
			}
		}
		if (same) {
			second = cur[0];
			ans.second = second;
			return ans;
		}
		else {
			vector<int> temp;
			for (int i = 1; i < cur.size(); i++) {
				temp.push_back(cur[i] - cur[i - 1]);
			}
			ans = ADA(temp);
			ans.second = cur[cur.size() - 1] + ans.second;
			ans.first += 1;
			return ans;
		}
	}
	else {
		if (cur.size() == 0) {
			return ans;
		}
		else {

			ans.second = cur[0];
			return ans;


		}
	}
}
int main() {
	int nP;
	cin >> nP;
	vector<int> V;
	for (int i = 0; i < nP; i++) {
		int temp;
		cin >> temp;
		V.push_back(temp);

	}
	pair<int, int> temp = ADA(V);
	cout << temp.first << " " << temp.second;
}
