#include<iostream>
using namespace std;

int main()
{
	int n, num[20];

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}
	
	for (int i = 0; i < n; i++)
	{
		if (num[i] % 2 == 0)
			cout << num[i] << " is even" << endl;
		else
			cout << num[i] << " is odd" << endl;
	}
	
	return 0;
}
