#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
 int a,b;
 vector<int> wins;
 int temp;
 
 cin>>a;
 cin >> b;
 for(int i =0;i<b;i++){
     cin >> temp;
     wins.push_back(temp);
 }
 
 sort(wins.begin(),wins.end());
 int cur = 0; int dist=0;
 for(int i =0;i<a;i++){
     if(cur<wins.size()){
         if (i==wins[cur]){
             while(wins[cur]==wins[cur+1]){
                 cur++;
             }
             dist++;
             cur++;
             
             continue;
         }
     }
     cout << i << endl;
 }
 cout << "Mario got " << dist <<" of the dangerous obstacles.";
}
