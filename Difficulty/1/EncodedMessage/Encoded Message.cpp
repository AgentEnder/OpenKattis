#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T;
	vector<string> ans;
	cin >> T;
	for (int t = 0; t < T; t++) {
		string temp;
		cin >> temp;
		string newArr = "";

		int matrixL = temp.length();
		matrixL = sqrt(matrixL);
		for (int j = matrixL-1; j >= 0; j--) {
			for (int i = 0; i < matrixL; i++) {
				newArr += temp[i*matrixL + j];

			}
		}
		ans.push_back(newArr);
	}

	for (int t = 0; t < T; t++) {
		cout << ans[t]<<endl;
	}
}