#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int main()
{
    int n, num[10], ogNum[10], ogPow[10];
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        string x = to_string(num[i]);
        string temp = x;
        int holder = stoi(x);
        x.erase(x.begin() + x.size()-1);
        //cout << x << endl;
        ogNum[i] = stoi(x);
        temp.erase(temp.begin(), temp.end()-1);
        //cout << temp << endl;
        ogPow[i] = stoi(temp);
        sum += pow(ogNum[i], ogPow[i]);
    }

    cout << sum;

    return 0;
}
