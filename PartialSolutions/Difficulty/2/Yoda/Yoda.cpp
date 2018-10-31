#include <iostream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

int main() {
	string a, b;
	int maxa, maxb;
	queue<char> aq, bq;
	cin >> a >> b;
	int minMax = min(maxa, maxb);
	minMax--; maxa--; maxb--;
	while (minMax >= 0) {
		if (a[maxa] > b[maxb]) {
			aq.push(a[maxa] );
			
		}
		else
		{
			bq.push(b[maxb]);
		}
		maxa--; maxb--; minMax--;
		a = a.substr(0, a.length() - 1); b = b.substr(0, b.length());
	}
	while (a.length()>0)
	{
		aq.push(a[a.length()]);
		a = a.substr(0, a.length() - 1);
	}

	while (b.length()>0)
	{
		bq.push(b[b.length()]);
		b = b.substr(0, b.length()-1);
	}
	if (aq.empty()) {
		cout << "Yoda"<<endl;

	}
	else {
		while (!aq.empty())
		{
			cout << aq.front();
			aq.pop();
		}
		cout << endl;
	}
	if (bq.empty()) {
		cout << "Yoda" << endl;
	}
	else {
		while (!aq.empty())
		{
			cout << aq.front();
			aq.pop();
		}
	}
	cin.get(); cin.get(); cin.get();
}
