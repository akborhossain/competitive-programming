#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main()
{
    string s="hello";
    string s1;
    cin>>s1;
    int si=0,i=0;
    for(char c: s1)
    {
       if(s[i]==c && si<=5){
        i++;
        si++;
       }

    }
    if(si==5)
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }

}
