#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL);

void Solve(){
    ll n;
    cin>>n;
    unordered_set<int>s;
    int a[n],b[n-1];
    for (int i=0;i<n;i++){
        cin>>a[i];
        s.insert(a[i]);
    }
    
    for (int i=0;i<n-1;i++)
    cin>>b[i];

    sort(a,a+n);
    sort(b,b+n-1);
    ll ans=b[0]-a[1];
    for (int i=0;i<n-1;i++){
        if(s.count(b[i]-ans)==0)
        {
            ans=b[0]-a[0];
            break;
        }
    }
    if(ans <= 0) ans = b[0]-a[0];
    cout << ans << "\n";

}

int main(){
    fastio
    int n;
    cin>>n;
    while(n--)
    {
        Solve();
    }

return 0;
}