#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main()
{
    int n,m;
    cin>>n>>m;
    char color[n][m];
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            cin>>color[i][j];
        }
    }
    bool clr=false;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(color[i][j]=='Y' || color[i][j]=='M' || color[i][j]=='C'){
                clr=true;
            }
        }


    }
    if(clr){
        cout<<"#Color"<<endl;
    }else{
    cout<<"#Black&White"<<endl;
    }

}
