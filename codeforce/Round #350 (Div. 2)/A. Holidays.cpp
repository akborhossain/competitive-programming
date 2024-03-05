#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main()
{

    int n,mip,mxp,x,y;
    cin>>n;
    x=n%7;
    y=n/7;

    if(x==6)
    {
        mip=y*2+1;
    }
    else
    {
        mip=2*y;
    }
    if(x==1){
        mxp=2*y+1;
    }
    else if(x>=2){
        mxp=2*y+2;
    }
    else{
        mxp=2*y;
    }
    cout<< mip<<" " << mxp<<endl;

}
