#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, a[4], x;
    cin>>t;
    while(t--) {
        
        x = 0;

        for(int i=0; i<4; i++) {
            cin>>a[i];
        }

        sort(a,a+4);

        if(a[0]!=a[1]&&a[1]!=a[2]&&a[2]!=a[3])
         {
          cout<<2<<endl;
         }
         else if(a[0]!=a[1]&&a[1]!=a[2]&&a[2]==a[3]||a[0]!=a[1]&&a[1]==a[2]&&a[2]!=a[3]||a[0]==a[1]&&a[1]!=a[2]&&a[2]!=a[3]||a[0]==a[1]&&a[1]!=a[2]&&a[2]==a[3])
          {
            cout<<2<<endl;
          }
          else if(a[0]!=a[1]&&a[1]==a[2]&&a[2]==a[3]||a[0]==a[1]&&a[1]==a[2]&&a[2]!=a[3])
          {
            cout<<1<<endl;
          }
          else
          {
            cout<<0<<endl;
          }
         
    }

    return 0;
}