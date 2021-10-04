#include<bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin>>a>>b;
    string num[10] = {"","one","two","three","four","five","six","seven","eight","nine"};
    if ((a<=9) && (b<=9)){
        for(int i=a;i<=b;++i){
            cout<<num[i]<<endl;
        }
    }
    if ((a<=9) && (b>9)){
        for(int i=a;i<=9;++i){
            cout<<num[i]<<endl;
        
        }
        for (int i=10;i<=b;i++){
            if(i%2==0){
                cout<<"even"<<endl;
            }
            else{
                cout<<"odd"<<endl;
            }
        }
    }
    if ((a>9) && (b>9)){
        for (int i=a;i<=b;i++){
            if(i%2==0){
                cout<<"even"<<endl;
            }
            else{
                cout<<"odd"<<endl;
        
            }
        }
    }
        
        
    
    return 0;
}
