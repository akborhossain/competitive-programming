#include<iostream>
using namespace std;
int main()
{

    int n,i;
    i=0;
    cin>>n;
    int ar[101]= {};
    for(int i=0; i<n; i++)
    {
        int m;
        cin>>m;
        ar[m]++;

    }
    int r=0;
    for(int i=0; i<101; i++)
    {
        r+=ar[i]/2;
    }

    cout<<r<<endl;
    return 0;
}
