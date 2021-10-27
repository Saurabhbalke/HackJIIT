#include<bits/stdc++.h>
using namespace std;
void solve()
{
    int a,b;
    cin>>a>>b;
    
    int check=b;
    check++;
    if(b==a-1)
    {
        cout<<"-1"<<"\n";
        return;
    }
    
    int i;
    for(i=1;i<=a;i++)
    {
        if(b==0)
        break;
        cout<<i<<" ";
        b--;
    }

    
    vector<int>temp;
    for(int j=a; j>=i;j--)
    {
        if(j==check)
        {
            temp.push_back(j);
            continue;
        }
        cout<<j<<" ";
        check++;
        
    }
    for(auto val:temp)
    cout<<val<<" ";
    cout<<"\n";
    return;
    }
    
    int main()
    {
        int t;
        cin>>t;
        while(t--)
        {
            solve();
        }
    
    
    return 0;
}