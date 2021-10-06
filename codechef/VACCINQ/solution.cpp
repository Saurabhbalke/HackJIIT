#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long int t;
	cin>>t;
	while(t--)
	{
	    int n,p,x,y;
	    cin>>n>>p>>x>>y;
	   
	    int arr[n];
	    int count1=0,count2=0;
	    for(int i=1;i<=n;i++)
	    {
	        cin>>arr[i];
	        
	        
	    }
	    for(int i=1;i<=p;i++)
	    {
	        if(arr[i]==0)
	        {
	            count1+=x;
	        }
	        else{
	            count2+=y;
	        }
	        
	    }
	    cout<<count2+count1<<endl;
	    
	}
	return 0;
}
