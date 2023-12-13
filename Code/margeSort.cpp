#include<bits/stdc++.h>
#include<iostream>
using namespace std;
void marge(int *ar,int l,int m,int h)
{
    int i=l;
    int j=m+1;
    int k=l;
    int tem[h+1];
    while(i<=m && j<=h)
    {
        if(ar[i]<=ar[j])
        {
            tem[k]=ar[i];
            i++;

        }
        else
        {
            tem[k]=ar[j];

            j++;
        }
        k++;
    }
    if(i>m)
    {
        while(j<=h)
        {
            tem[k]=ar[j];
            k++;
            j++;
        }

    }
    else
    {
        while(i<=m)
        {
            tem[k]=ar[i];
            k++;
            i++;
        }

    }
    for(k=l; k<=h; k++)
    {
        ar[k]=tem[k];
    }
}
void margeSort(int *ar, int l, int h)
{
    if(l<h)
    {
        int m=(l+h)/2;
        margeSort(ar,l,m);
        margeSort(ar, m+1,h);
        marge(ar,l,m,h);
    }

}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    margeSort(arr,0,n-1);
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
}
