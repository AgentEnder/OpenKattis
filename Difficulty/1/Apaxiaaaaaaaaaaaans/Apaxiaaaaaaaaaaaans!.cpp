#include <iostream>
#include<string>
using namespace std;

int main() {
 
    string name;
    cin >> name;

    for (int i = 0; i < name.size(); i++)
    {
        while (name[i] == name[i + 1])
        {
            if (name[i] == name[i + 1])
            {
                name.erase(name.begin() + i + 1);
            }
        }
    }
    cout << name;
    return 0;
}
