#include<iostream>
#include<string>
using namespace std;

int main()
{
    long l, h, ch0, ch1, ch2, ch3, ch4, ch5, count = 0;

    cin >> l >> h;

    for (long i = l; i <= h; i++)
    {
        string temp = to_string(i);
        if ((temp.at(0) == (temp.at(1)) || (temp.at(0) == temp.at(2) )|| (temp.at(0) == temp.at(3)) || (temp.at(0) == temp.at(4)) || (temp.at(0) == temp.at(5))))
            continue;
        if ((temp.at(1) == (temp.at(0)) || (temp.at(1) == temp.at(2)) || (temp.at(1) == temp.at(3)) || (temp.at(1) == temp.at(4)) || (temp.at(1) == temp.at(5))))
            continue;
        if ((temp.at(2) == (temp.at(0)) || (temp.at(2) == temp.at(1)) || (temp.at(2) == temp.at(3)) || (temp.at(2) == temp.at(4)) || (temp.at(2) == temp.at(5))))
            continue;
        if ((temp.at(3) == (temp.at(0)) || (temp.at(3) == temp.at(1)) || (temp.at(3) == temp.at(2)) || (temp.at(3) == temp.at(4)) || (temp.at(3) == temp.at(5))))
            continue;
        if ((temp.at(4) == (temp.at(0)) || (temp.at(4) == temp.at(1)) || (temp.at(4) == temp.at(2)) || (temp.at(4) == temp.at(3)) || (temp.at(4) == temp.at(5))))
            continue;
        if ((temp.at(5) == (temp.at(0)) || (temp.at(5) == temp.at(1)) || (temp.at(5) == temp.at(2)) || (temp.at(5) == temp.at(3)) || (temp.at(5) == temp.at(4))))
            continue;
        if((temp.at(0) - 48)!=0)
            ch0 = i % (temp.at(0) - 48);
        else if ((temp.at(0) - 48) == 0)
            ch1 = -1;
        if ((temp.at(1) - 48) != 0)
            ch1 = i % (temp.at(1) - 48);
        else if ((temp.at(1) - 48) == 0)
            ch1 = -1;
        if ((temp.at(2) - 48) != 0)
            ch2 = i % (temp.at(2) - 48);
        else if ((temp.at(2) - 48) == 0)
            ch2 = -1;
        if ((temp.at(3) - 48) != 0)
            ch3 = i % (temp.at(3) - 48);
        else if ((temp.at(3) - 48) == 0)
            ch3 = -1;
        if ((temp.at(4) - 48) != 0)
            ch4 = i % (temp.at(4) - 48);
        else if ((temp.at(4) - 48) == 0)
            ch4 = -1;
        if ((temp.at(5) - 48) != 0)
            ch5 = i % (temp.at(5) - 48);
        else if ((temp.at(5) - 48) == 0)
            ch5 = -1;
        
        if ((ch0 == 0 )&&( ch1 == 0 )&&( ch2 == 0 )&& (ch3 == 0) && (ch4 == 0) &&( ch5 == 0))
        {
            count++;
            //cout << count << endl;
            //cout << i << endl;
        }
        if (h < i)
            break;
    }

    cout << count << endl;

    return 0;
}
