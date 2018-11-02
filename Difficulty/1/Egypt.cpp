#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int a[1000], b[1000], c[1000], count = 0;
    do 
    {
        cin >> a[count] >> b[count] >> c[count];
        count++;

    } while (a[count - 1] != 0 && b[count - 1] != 0 && c[count - 1] != 0);

    for (int i = 0; i < count; i++)
    {
        int x = a[i], y = b[i], z = c[i];
        if (((pow(x, 2) + pow(y, 2) == pow(z, 2)) || (pow(x, 2) + pow(z, 2) == pow(y, 2)) || (pow(z, 2) + pow(y, 2) == pow(x, 2)))&&((x != 0 && y != 0 && z != 0)))
            cout << "right" << endl;
        else if (x == 0 && y == 0 && z == 0)
            break;
        else
            cout << "wrong" << endl;
    }

    return 0;
}
