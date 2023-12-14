
#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int partit(int *ar,int l,int h)
{
    int i=l,j=h,p=ar[l];
    while(i<j)
    {

        while(ar[i]<=p)
        {
            i++;
        }
        while(ar[j]>p)
        {
            j--;
        }
        if(i<j)
        {
            int tem=ar[i];
            ar[i]=ar[j];
            ar[j]=tem;
        }
    }
    int tem=ar[l];
    ar[l]=ar[j];
    ar[j]=tem;
    return j;

}
void quick(int *ar,int l,int h){
    if(l<h){
        int j=partit(ar,l,h);
        quick(ar,l,j-1);
        quick(ar,j+1,h);
    }

}
int main(){
int n;
cin>>n;
int ar[n];
for(int i=0;i<n;i++){
    cin>>ar[i];
}
quick(ar,0,n-1);
for(int i=0;i<n;i++){
    cout<<ar[i]<<" ";
}
}
