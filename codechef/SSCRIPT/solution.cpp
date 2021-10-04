#include <bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define ll long long

int main() {
    int t;
    cin>>t;
    while(t--){
        ll n,k;
        cin>>n>>k;
        string s;
        cin>>s;
        ll i=0;
        bool flag=false;
        while(i<n){
           // cout<<"The value of i here is= "<<i<<endl;
            if(s[i]=='*')  {
                ll j=i+1;
                ll o=1;
                while(j<n && s[j]=='*') {
                     
                    j++;
                    
                }
                o+=j-i-1;
                if(o==k){
                      flag=true;  
                      break;
                    } 
                i=j+1;
               
            }
            else i++;
            
            
        }
        if(flag) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
	return 0;
}
