#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned int ui;
typedef unsigned long long int ul;

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	ui test;
	cin >> test;
	while(test--){
	    string s;
	    cin >> s;
	    char status = '1';
	    ll count = 0;
	    for(auto it = s.begin(); it != s.end(); ++it){
	        if((*it) != status){
	            count++;
	            status = (*it);
	        }
	    }
	    cout << count << "\n";
	}
	return 0;
}
